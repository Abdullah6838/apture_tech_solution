import csv
import json
import os
from datetime import datetime

def extract_data(input_file: str) -> list:
    """Reads raw CSV records into memory."""
    if not os.path.exists(input_file):
        raise FileNotFoundError(f"Input file '{input_file}' not found.")
    
    with open(input_file, mode="r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)

def validate_and_clean_data(raw_data: list):
    """Validates data rules, routes bad records to errors, and cleans valid ones."""
    clean_records = []
    error_records = []
    
    for idx, row in enumerate(raw_data, start=1):
        errors = []
        
        # Validate ID
        if not row.get("id") or not row["id"].strip():
            errors.append("Missing ID")
        
        # Validate Price
        try:
            price = float(row.get("price", 0))
            if price < 0:
                errors.append("Negative price")
        except ValueError:
            errors.append("Invalid price format")
            price = 0.0

        # Validate Quantity
        try:
            quantity = int(row.get("quantity", 0))
            if quantity < 0:
                errors.append("Negative quantity")
        except ValueError:
            errors.append("Invalid quantity format")
            quantity = 0

        # Separate clean rows from malformed ones
        if errors:
            error_entry = row.copy()
            error_entry["row_number"] = idx
            error_entry["error_reasons"] = "; ".join(errors)
            error_records.append(error_entry)
        else:
            cleaned_row = {
                "id": row["id"].strip(),
                "name": row.get("name", "").strip().title(),
                "price": price,
                "quantity": quantity,
                "category": row.get("category", "General").strip().capitalize()
            }
            clean_records.append(cleaned_row)
            
    return clean_records, error_records

def transform_data(clean_records: list) -> list:
    """Computes calculated fields and timestamps."""
    for record in clean_records:
        record["total_value"] = round(record["price"] * record["quantity"], 2)
        record["processed_at"] = datetime.now().isoformat()
    return clean_records

def generate_summary(clean_records: list, error_records: list) -> dict:
    """Calculates summary metrics for reporting."""
    if not clean_records:
        return {"total_records": 0, "total_revenue": 0.0}

    total_items = len(clean_records)
    total_revenue = sum(r["total_value"] for r in clean_records)
    avg_price = sum(r["price"] for r in clean_records) / total_items

    return {
        "execution_timestamp": datetime.now().isoformat(),
        "total_clean_records": total_items,
        "total_error_records": len(error_records),
        "total_inventory_revenue": round(total_revenue, 2),
        "average_product_price": round(avg_price, 2)
    }

def load_data(clean_records: list, error_records: list, clean_output: str, error_output: str):
    """Exports clean records to CSV and errors to JSON."""
    if clean_records:
        keys = clean_records[0].keys()
        with open(clean_output, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(clean_records)

    with open(error_output, mode="w", encoding="utf-8") as f:
        json.dump(error_records, f, indent=4)

def run_pipeline(input_file: str, clean_output: str, error_output: str) -> dict:
    """Orchestrates the complete procedural pipeline execution."""
    raw_data = extract_data(input_file)
    clean_records, error_records = validate_and_clean_data(raw_data)
    clean_records = transform_data(clean_records)
    summary = generate_summary(clean_records, error_records)
    load_data(clean_records, error_records, clean_output, error_output)
    
    print(f"Pipeline complete. Clean data saved to {clean_output}, errors logged to {error_output}.")
    return summary

if __name__ == "__main__":
    summary_report = run_pipeline("raw_input.csv", "clean_dataset.csv", "error_log.json")
    print("\nPipeline Summary Report:")
    print(json.dumps(summary_report, indent=4))