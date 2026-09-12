# 🧹 Data Cleaning and ETL Pipeline

## 📌 Project Overview

The **Data Cleaning and ETL Pipeline** is a Python-based data processing project designed to read raw product data from a CSV file, validate and clean the records, transform valid data, generate summary statistics, and save the results into output files.

The project follows the **ETL (Extract, Transform, Load)** process:

```text
📥 Extract → 🔍 Validate & Clean → 🔄 Transform → 📊 Summarize → 💾 Load
````

 The pipeline separates valid records from invalid records.

 - ✅ Clean records are saved to `clean_dataset.csv`
- ❌ Invalid records are saved to `error_log.json`

---

 # 🎯 Objectives

 The main objectives of this project are:

 - 📥 Read raw data from a CSV file.
- 🔍 Validate important product fields.
- ❌ Identify invalid or malformed records.
- 🧹 Clean valid records.
- 🔢 Convert price and quantity into appropriate numeric types.
- 🧮 Calculate the total value of each product.
- 🕒 Add processing timestamps.
- 📊 Generate summary statistics.
- 💾 Save clean data into a CSV file.
- 📝 Save invalid records into a JSON error log.
- 🐍 Practice Python programming and file handling.

---

 # ✨ Features

 ## 📥 Extract Raw Data

 The application reads raw product information from:

```
📄 raw_input.csv
```

 The CSV file is processed using Python's built-in `csv` module.

---

 ## 🔍 Validate Data

 The pipeline validates the following fields:

 - 🆔 Product ID
- 💰 Product Price
- 📦 Product Quantity

 It detects:

 - ⚠️ Missing IDs
- 🔴 Negative prices
- ❌ Invalid price formats
- 🔴 Negative quantities
- ❌ Invalid quantity formats

---

 ## 🧹 Clean Data

 Valid records are cleaned by:

 - ✂️ Removing unnecessary whitespace.
- 🔤 Formatting product names using title case.
- 🔤 Formatting categories using capitalization.
- 💰 Converting prices to `float`.
- 📦 Converting quantities to `int`.

---

 ## ❌ Error Handling

 Invalid records are separated from valid records.

 Each error record contains:

 - 📄 Original row data
- 🔢 Row number
- ⚠️ Error reason(s)

 Invalid records are stored in:

```
📝 error_log.json
```

---

 ## 🔄 Transform Data

 For every valid record, the pipeline calculates:

```
🧮 total_value = price × quantity
```

 A processing timestamp is also added:

```
🕒 processed_at
```

---

 ## 📊 Generate Summary

 The pipeline generates statistics including:

 - 🕒 Execution timestamp
- ✅ Total clean records
- ❌ Total error records
- 💰 Total inventory revenue/value
- 📊 Average product price

---

 ## 💾 Load Output Data

 Clean records are saved to:

```
📄 clean_dataset.csv
```

 Invalid records are saved to:

```
📝 error_log.json
```

---

 # 🛠️ Technologies Used

 | 🧰 Technology | 📌 Purpose |
| --- | --- |
| 🐍 Python 3 | Main programming language |
| 📄 CSV | Reading and writing tabular data |
| 📝 JSON | Error logging and data storage |
| 📁 `os` | File existence checking |
| 🕒 `datetime` | Processing timestamps |

 The project uses only Python's **built-in libraries**.

```
import csv
import json
import os
from datetime import datetime
```

---

 # 📁 Project Structure

```
📂 Task 2/
│
├── 🐍 Task_2.py
├── 📥 raw_input.csv
├── ✅ clean_dataset.csv
├── ❌ error_log.json
└── 📖 Readme.md
```

 ## 📄 File Description

 ### 🐍 `Task_2.py`

 Contains the complete Python ETL/data-cleaning pipeline.

 ### 📥 `raw_input.csv`

 Contains the original raw input product data.

 ### ✅ `clean_dataset.csv`

 Contains successfully validated, cleaned, and transformed records.

 ### ❌ `error_log.json`

 Contains invalid records along with the reasons why they failed validation.

 ### 📖 `Readme.md`

 Contains the project documentation and instructions.

---

 # 🔄 ETL Pipeline

 The application follows these main stages:

```
                 📥 raw_input.csv
                        │
                        ▼
                 📤 Extract Data
                        │
                        ▼
                🔍 Validate & Clean
                        │
                 ┌──────┴──────┐
                 │             │
                 ▼             ▼
             ✅ Valid       ❌ Invalid
              Records        Records
                 │             │
                 ▼             ▼
            🔄 Transform   📝 Error Log
                 │             │
                 ▼             ▼
          📄 Clean CSV      📋 JSON File
                 │
                 ▼
             📊 Summary
```

---

 # 🧩 Functions

 The program contains several functions, with each function responsible for a specific stage of the pipeline.

---

 ## 1️⃣ `extract_data()`

```
def extract_data(input_file: str) -> list:
```

 ### 🎯 Purpose

 Reads raw records from the input CSV file.

 ### 📥 Input

```
raw_input.csv
```

 ### 📤 Returns

 A list containing all CSV records.

 ### 💻 Example

```
raw_data = extract_data("raw_input.csv")
```

 If the file does not exist, a `FileNotFoundError` is raised.

---

 # 2️⃣ `validate_and_clean_data()`

```
def validate_and_clean_data(raw_data: list):
```

 ### 🎯 Purpose

 Validates raw records and separates them into:

 - ✅ Clean records
- ❌ Error records

---

 ## 🆔 Product ID Validation

 The Product ID must exist and cannot be empty.

 Invalid example:

```
id = ""
```

 Error:

```
❌ Missing ID
```

---

 ## 💰 Price Validation

 The price must:

 - 🔢 Be numeric
- 🚫 Not be negative

 Valid example:

```
750.50
```

 Invalid example:

```
-100
```

 Error:

```
❌ Negative price
```

 Invalid format:

```
abc
```

 Error:

```
❌ Invalid price format
```

---

 ## 📦 Quantity Validation

 The quantity must:

 - 🔢 Be an integer
- 🚫 Not be negative

 Valid example:

```
10
```

 Invalid example:

```
-5
```

 Error:

```
❌ Negative quantity
```

 Invalid format:

```
abc
```

 Error:

```
❌ Invalid quantity format
```

---

 # 🧹 Data Cleaning

 For valid records, the pipeline performs several cleaning operations.

 ## 🆔 Product ID

 Leading and trailing spaces are removed.

 Example:

```
" P001 "
```

 becomes:

```
"P001"
```

 Using:

```
row["id"].strip()
```

---

 ## 🏷️ Product Name

 Names are stripped and converted to title case.

 Example:

```
"gaming laptop"
```

 becomes:

```
"Gaming Laptop"
```

 Using:

```
row.get("name", "").strip().title()
```

---

 ## 🗂️ Category

 Categories are stripped and capitalized.

 Example:

```
"electronics"
```

 becomes:

```
"Electronics"
```

---

 ## 💰 Price

 Price values are converted to `float`.

 Example:

```
"750.50"
```

 becomes:

```
750.5
```

---

 ## 📦 Quantity

 Quantity values are converted to `int`.

 Example:

```
"10"
```

 becomes:

```
10
```

---

 # 3️⃣ `transform_data()`

```
def transform_data(clean_records: list) -> list:
```

 ### 🎯 Purpose

 Adds calculated fields to each clean record.

 Two additional fields are created:

```
🧮 total_value
🕒 processed_at
```

---

 ## 🧮 Total Value

 The total value is calculated using:

```
total_value = price × quantity
```

 ### Example

```
💰 Price = 100
📦 Quantity = 5
```

 Calculation:

```
100 × 5 = 500
```

 Result:

```
🧮 total_value = 500.00
```

 The Python code is:

```
record["total_value"] = round(
    record["price"] * record["quantity"],
    2
)
```

---

 ## 🕒 Processing Timestamp

 Each clean record receives a timestamp.

 Example:

```
2026-09-11T21:30:00.123456
```

 The timestamp is created using:

```
datetime.now().isoformat()
```

---

 # 4️⃣ `generate_summary()`

```
def generate_summary(clean_records: list, error_records: list) -> dict:
```

 ### 🎯 Purpose

 Generates a summary of the pipeline execution.

 The summary contains:

 - 🕒 Execution timestamp
- ✅ Total clean records
- ❌ Total error records
- 💰 Total inventory revenue
- 📊 Average product price

 ### 📊 Example

```
{
    "execution_timestamp": "2026-09-11T21:30:00.123456",
    "total_clean_records": 5,
    "total_error_records": 2,
    "total_inventory_revenue": 12500.0,
    "average_product_price": 350.5
}
```

---

 # 5️⃣ `load_data()`

```
def load_data(
    clean_records,
    error_records,
    clean_output,
    error_output
):
```

 ### 🎯 Purpose

 Writes the processed results to output files.

 ### ✅ Clean Data

 Clean records are written to:

```
📄 clean_dataset.csv
```

 ### ❌ Error Data

 Error records are written to:

```
📝 error_log.json
```

---

 # 6️⃣ `run_pipeline()`

```
def run_pipeline(
    input_file,
    clean_output,
    error_output
) -> dict:
```

 ### 🎯 Purpose

 This function controls the entire pipeline.

 It executes the stages in the following order:

```
1️⃣ Extract
     ↓
2️⃣ Validate
     ↓
3️⃣ Clean
     ↓
4️⃣ Transform
     ↓
5️⃣ Generate Summary
     ↓
6️⃣ Load
```

 The function also prints a completion message and returns the summary report.

---

 # 📥 Input File

 The application expects the input file:

```
📄 raw_input.csv
```

 The CSV should contain fields such as:

```
id,name,price,quantity,category
```

 ### 📝 Example Input

```
id,name,price,quantity,category
P001,laptop,750,10,electronics
P002,keyboard,35,25,accessories
P003,mouse,20,30,accessories
P004,monitor,250,8,electronics
```

---

 # 🧹 Data Cleaning Example

 Suppose the raw input contains:

```
id,name,price,quantity,category
 P001 ,gaming laptop,750.50,10,electronics
P002,keyboard,35,25,accessories
```

 After cleaning, the data becomes:

```
id,name,price,quantity,category,total_value,processed_at
P001,Gaming Laptop,750.5,10,Electronics,7505.0,2026-09-11T...
P002,Keyboard,35.0,25,Accessories,875.0,2026-09-11T...
```

---

 # ❌ Error Log

 Invalid records are stored in:

```
📝 error_log.json
```

 ### Example

```
[
    {
        "id": "P005",
        "name": "Broken Product",
        "price": "-50",
        "quantity": "10",
        "category": "Test",
        "row_number": 5,
        "error_reasons": "Negative price"
    },
    {
        "id": "",
        "name": "Unknown Product",
        "price": "20",
        "quantity": "5",
        "category": "General",
        "row_number": 6,
        "error_reasons": "Missing ID"
    }
]
```

 The error log preserves the original information and adds:

```
🔢 row_number
⚠️ error_reasons
```

---

 # 📄 Output File

 The clean data is stored in:

```
✅ clean_dataset.csv
```

 ### Example

```
id,name,price,quantity,category,total_value,processed_at
P001,Laptop,750.0,10,Electronics,7500.0,2026-09-11T21:30:00
P002,Keyboard,35.0,25,Accessories,875.0,2026-09-11T21:30:00
P003,Mouse,20.0,30,Accessories,600.0,2026-09-11T21:30:00
```

---

 # 📊 Pipeline Summary Report

 After processing, the program displays:

```
✅ Pipeline complete.
📄 Clean data saved to clean_dataset.csv
📝 Errors logged to error_log.json

📊 Pipeline Summary Report:

{
    "execution_timestamp": "...",
    "total_clean_records": 4,
    "total_error_records": 2,
    "total_inventory_revenue": 8975.0,
    "average_product_price": 263.75
}
```

---

 # 🧪 Example Error Scenarios

 ## ❌ Missing ID

 Input:

```
,Keyboard,35,10,Accessories
```

 Result:

```
❌ Missing ID
```

 The record is moved to `error_log.json`.

---

 ## 🔴 Negative Price

 Input:

```
P001,Laptop,-750,10,Electronics
```

 Result:

```
❌ Negative price
```

 The record is considered invalid.

---

 ## ❌ Invalid Price

 Input:

```
P001,Laptop,abc,10,Electronics
```

 Result:

```
❌ Invalid price format
```

---

 ## 🔴 Negative Quantity

 Input:

```
P001,Laptop,750,-10,Electronics
```

 Result:

```
❌ Negative quantity
```

---

 ## ❌ Invalid Quantity

 Input:

```
P001,Laptop,750,abc,Electronics
```

 Result:

```
❌ Invalid quantity format
```

---

 # ⚠️ Multiple Errors in One Record

 A single record can contain multiple validation errors.

 Example:

```
,Laptop,-750,-10,Electronics
```

 The error log may contain:

```
⚠️ Missing ID; Negative price; Negative quantity
```

 This allows multiple problems in the same record to be identified.

---

 # 📊 Example Calculations

 ## 🧮 Total Product Value

 For a product:

```
💰 Price = $50
📦 Quantity = 20
```

 Calculation:

```
50 × 20 = $1,000
```

 Therefore:

```
🧮 Total Value = $1,000.00
```

---

 ## 📊 Average Product Price

 If the products have prices:

```
💰 100
💰 200
💰 300
```

 The average price is:

```
(100 + 200 + 300) / 3
= 200
```

 Therefore:

```
📊 Average Price = $200.00
```

---

 ## 💰 Total Inventory Revenue

 If the total values are:

```
💰 1000
💰 2500
💰 750
```

 Then:

```
1000 + 2500 + 750 = 4250
```

 Therefore:

```
💰 Total Inventory Revenue = $4,250.00
```

---

 # 🚀 How to Run the Project

 ## 1️⃣ Install Python

 Make sure **Python 3** is installed on your computer.

 Check the Python version:

```
python --version
```

 Or:

```
python3 --version
```

---

 ## 2️⃣ Open the Project Folder

 Open a terminal or command prompt and navigate to the Task 2 folder:

```
cd "Task 2"
```

---

 ## 3️⃣ Check the Input File

 Make sure this file exists:

```
📥 raw_input.csv
```

---

 ## 4️⃣ Run the Program

 Run:

```
python "Task_2.py"
```

 Or:

```
python3 "Task_2.py"
```

---

 # 🖥️ Expected Output

 After successful execution, the terminal displays:

```
✅ Pipeline complete. Clean data saved to clean_dataset.csv, errors logged to error_log.json.

📊 Pipeline Summary Report:

{
    "execution_timestamp": "...",
    "total_clean_records": 4,
    "total_error_records": 1,
    "total_inventory_revenue": 8975.0,
    "average_product_price": 263.75
}
```

---

 # 🔄 Program Workflow

```
🚀 Start
   │
   ▼
📥 Read raw_input.csv
   │
   ▼
📤 Extract Records
   │
   ▼
🔍 Validate Records
   │
   ├─────────────────────┐
   │                     │
   ▼                     ▼
✅ Valid Records      ❌ Invalid Records
   │                     │
   ▼                     ▼
🧹 Clean Records      📝 Error Log
   │                     │
   ▼                     ▼
🔄 Transform Data     💾 Save JSON
   │
   ▼
🧮 Calculate Total Value
   │
   ▼
🕒 Add Timestamp
   │
   ▼
💾 Save Clean CSV
   │
   ▼
📊 Generate Summary
   │
   ▼
🏁 End
```

---

 # 🧠 Concepts Demonstrated

 This project demonstrates several important Python concepts:

 - 🐍 Python functions
- 📋 Lists
- 📖 Dictionaries
- 🔁 Loops
- 🔀 Conditional statements
- 🛡️ Exception handling
- 📂 File handling
- 📄 CSV processing
- 📝 JSON processing
- 🔍 Data validation
- 🧹 Data cleaning
- 🔄 Data transformation
- 🧮 Calculated fields
- 🕒 Timestamps
- ❌ Error logging
- 📊 Summary reporting
- 🔄 ETL pipeline design

---

 # 🧰 Built-in Python Modules

 The project uses only Python's standard library:

```
import csv
import json
import os
from datetime import datetime
```

 ### 📄 `csv`

 Used for:

 - Reading CSV files
- Writing CSV files

 ### 📝 `json`

 Used for:

 - Writing error logs
- Displaying the summary report

 ### 📁 `os`

 Used to check whether the input file exists.

 ### 🕒 `datetime`

 Used to create processing timestamps.

---

 # ⚙️ Requirements

 The project requires:

```
🐍 Python 3.x
```

 No external packages are required.

 The application uses only Python's built-in modules.

---

 # 🧪 Testing Checklist

 The following test cases can be used to test the application:

 | 🧪 Test Case | ✅ Expected Result |
| --- | --- |
| Valid ID | Record accepted |
| Missing ID | Error logged |
| Positive price | Record accepted |
| Negative price | Error logged |
| Invalid price | Error logged |
| Positive quantity | Record accepted |
| Negative quantity | Error logged |
| Invalid quantity | Error logged |
| Extra spaces | Spaces removed |
| Lowercase name | Converted to title case |
| Lowercase category | Capitalized |
| Valid record | Added to clean CSV |
| Invalid record | Added to error JSON |

---

 # 📌 Important Notes

 - 📥 `raw_input.csv` must exist before running the program.
- 📋 The input CSV should contain the required columns.
- ✅ Clean records are saved to `clean_dataset.csv`.
- ❌ Invalid records are saved to `error_log.json`.
- 🔄 Running the pipeline may overwrite existing output files.
- 💰 Prices are converted to `float`.
- 📦 Quantities are converted to `int`.
- 🏷️ Product names are converted to title case.
- 🗂️ Categories are capitalized.
- 🧮 Total value is calculated using `price × quantity`.
- 🕒 Processing timestamps are added to clean records.

---

 # 🔐 Error Handling

 The pipeline includes error handling for missing input files and invalid data.

 If the input file does not exist:

```
❌ FileNotFoundError:
Input file 'raw_input.csv' not found.
```

 Invalid data is not added to the clean dataset.

 Instead, it is stored in:

```
📝 error_log.json
```

 with a clear explanation of the error.

---

 # 📸 Screenshot

 A screenshot of the project can be included in the Task 2 folder.

 Recommended file:

```
🖼️ Screenshot.png
```

 The screenshot can show the terminal output and pipeline summary.

---

 # 🔮 Future Improvements

 Possible improvements for this project include:

 - 🖥️ Create a Graphical User Interface (GUI)
- 🗄️ Add database integration
- 📊 Generate graphical reports
- 📈 Create charts for inventory data
- 📥 Add Excel file support
- 📤 Export reports to Excel or PDF
- 🔎 Add advanced validation rules
- 🔢 Detect duplicate Product IDs
- 🧹 Handle missing product names
- 📝 Add detailed logging
- 🧪 Add automated unit tests
- ⚡ Improve processing of large CSV files
- 📧 Send error reports by email
- 💾 Add automatic data backup
- 📊 Create an interactive dashboard

---

 # 🎓 Learning Outcomes

 After completing this project, the following skills are demonstrated:

 1. 📥 Reading CSV files using Python.
2. 📤 Writing CSV files using Python.
3. 📝 Reading and writing JSON files.
4. 🔍 Validating raw data.
5. 🧹 Cleaning inconsistent data.
6. ❌ Handling invalid records.
7. 🧮 Creating calculated fields.
8. 🕒 Working with timestamps.
9. 📊 Generating summary statistics.
10. 🔄 Building an ETL pipeline.
11. 🛡️ Handling exceptions.
12. 🧩 Organizing Python code into reusable functions.

---

 # 📂 Final Project Structure

```
📂 Task 2
│
├── 🐍 Task_2.py
├── 📥 raw_input.csv
├── ✅ clean_dataset.csv
├── ❌ error_log.json
└── 📖 Readme.md
```

---

 # 👨‍💻 Author

 ## 🎓 Task 2 - Data Cleaning and ETL Pipeline

 🐍 Developed using **Python 3**

---

 # 📄 License

 This project is created for:

 🎓 **Educational and Learning Purposes**

---

 # ⭐ Conclusion

 The **Data Cleaning and ETL Pipeline** provides a structured and efficient way to process raw CSV data.

 The complete pipeline is:

```
📥 Extract
    ↓
🔍 Validate
    ↓
🧹 Clean
    ↓
🔄 Transform
    ↓
📊 Generate Summary
    ↓
💾 Load
```

 ✅ Valid records are transformed and saved to:

```
clean_dataset.csv
```

 ❌ Invalid records are separated and saved to:

```
error_log.json
```

 This project demonstrates practical Python skills in:

 🐍 **Python Programming**\
 📄 **CSV Processing**\
 📝 **JSON Handling**\
 🔍 **Data Validation**\
 🧹 **Data Cleaning**\
 🔄 **Data Transformation**\
 ❌ **Error Handling**\
 📊 **Summary Reporting**\
 🔄 **ETL Pipeline Development**
