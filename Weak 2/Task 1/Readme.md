# 💰 CLI Expense Tracker

A simple command-line expense tracker built with 🐍 Python.

## ✨ Features

- ➕ Add expenses
- 📋 List expenses
- 🔍 Search expenses
- 🏷️ Filter by category
- 📊 View monthly totals
- 📅 Set custom expense dates
- 💾 Save data in `expenses.json`
- ⚠️ Validate amounts and dates

## 🛠️ Requirements

- 🐍 Python 3.7+
- 📦 No external libraries required

## 📁 Project Structure

```text
Task 1/
├── 🐍 Task 1.py
├── 💾 expenses.json
├── 📷 Screenshot.png
└── 📖 Readme.md
```

## 💾 Data Store Format

The expense data is stored in a local `expenses.json` file.

### 📄 Example `expenses.json`

```json
[
    {
        "id": 1,
        "date": "2026-09-07",
        "amount": 25.5,
        "category": "food",
        "description": "Lunch"
    },
    {
        "id": 2,
        "date": "2026-09-07",
        "amount": 50.0,
        "category": "transport",
        "description": "Taxi ride"
    },
    {
        "id": 3,
        "date": "2026-09-06",
        "amount": 15.0,
        "category": "entertainment",
        "description": "Movie"
    }
]
```
<br>

# 🚀 How to Run

Make sure Python is installed:

```bash
python run Task 1.py
