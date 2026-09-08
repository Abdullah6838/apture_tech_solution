import csv
import requests

API_URL = "https://fakestoreapi.com/products"
CSV_OUTPUT = "cleaned_products.csv"

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Connection error occurred: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout error occurred: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"An unexpected error occurred: {req_err}")
    return None

def process_and_clean_data(raw_data):
    cleaned_data = []
    seen_ids = set()
    
    for item in raw_data:
        prod_id = item.get("id")
        title = item.get("title")
        price = item.get("price")
        category = item.get("category")
        rating_obj = item.get("rating", {})
        rate = rating_obj.get("rate")
        
        # Data cleaning and validation rules
        if not prod_id or prod_id in seen_ids:
            continue
        if price is None or price < 0:
            continue
        if not title:
            title = "Unknown Product"
        else:
            title = title.strip()
        if not category:
            category = "General"
        else:
            category = category.strip().title()
        if rate is None:
            rate = 0.0
            
        seen_ids.add(prod_id)
        
        cleaned_data.append({
            "id": prod_id,
            "title": title,
            "price": float(price),
            "category": category,
            "rating": float(rate)
        })
        
    return cleaned_data

def calculate_statistics(data):
    if not data:
        return {}
        
    total_products = len(data)
    prices = [item["price"] for item in data]
    avg_price = sum(prices) / total_products
    max_price = max(prices)
    min_price = min(prices)
    
    category_stats = {}
    for item in data:
        cat = item["category"]
        if cat not in category_stats:
            category_stats[cat] = {"count": 0, "total_price": 0.0}
        category_stats[cat]["count"] += 1
        category_stats[cat]["total_price"] += item["price"]
        
    for cat, stats in category_stats.items():
        stats["avg_price"] = stats["total_price"] / stats["count"]
        
    return {
        "total_products": total_products,
        "avg_price": avg_price,
        "max_price": max_price,
        "min_price": min_price,
        "category_stats": category_stats
    }

def export_to_csv(data, filename):
    if not data:
        print("No data available to export.")
        return
        
    fieldnames = ["id", "title", "price", "category", "rating"]
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            for row in data:
                writer.writerow(row)
        print(f"\nData successfully exported to {filename}")
    except IOError as e:
        print(f"Failed to write CSV file: {e}")

def main():
    print("Fetching data from API...")
    raw_data = fetch_api_data(API_URL)
    
    if raw_data:
        print(f"Successfully fetched {len(raw_data)} records. Cleaning data...")
        cleaned_data = process_and_clean_data(raw_data)
        print(f"Retained {len(cleaned_data)} valid records after cleaning.")
        
        print("Calculating summary statistics...")
        stats = calculate_statistics(cleaned_data)
        
        print("\n=== Summary Statistics ===")
        print(f"Total Products: {stats['total_products']}")
        print(f"Average Price:  ${stats['avg_price']:.2f}")
        print(f"Highest Price:  ${stats['max_price']:.2f}")
        print(f"Lowest Price:   ${stats['min_price']:.2f}")
        
        print("\nCategory Breakdown:")
        for cat, details in stats['category_stats'].items():
            print(f"  - {cat}: {details['count']} items | Avg Price: ${details['avg_price']:.2f}")
            
        export_to_csv(cleaned_data, CSV_OUTPUT)
    else:
        print("Process terminated due to API fetch failure.")

if __name__ == "__main__":
    main()
