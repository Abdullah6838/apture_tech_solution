# 📦 Inventory Management System 

## 📌 Project Overview

The **Inventory Management System** is a simple command-line application developed using **Python**. It is designed to help users manage products in an inventory efficiently.

The system allows users to add, delete, update, search, and display products. All inventory information is stored in a **JSON file**, allowing the data to remain available even after the application is closed.

---

## 🎯 Objectives

The main objectives of this project are:

- To create a simple inventory management application.
- To practice **Object-Oriented Programming (OOP)** in Python.
- To store and manage data using **JSON**.
- To implement CRUD operations:
  - Create
  - Read
  - Update
  - Delete
- To validate user input.
- To provide a simple and user-friendly command-line interface.

---

## ✨ Features

The application provides the following features:

### ➕ Add Product
Add a new product to the inventory using:

- Product ID
- Product Name
- Price
- Quantity
- Category

### 🗑️ Delete Product
Delete an existing product by entering its Product ID.

### ✏️ Edit Product Details
Update the details of an existing product, including:

- Product Name
- Price
- Quantity
- Category

Users can leave a field blank if they do not want to change that particular value.

### 🔍 Search Product
Search for products using:

- Product ID
- Product Name
- Category

The search is case-insensitive.

### 📋 View All Products
Display all available products in a formatted table.

### 💾 Automatic Data Storage
All changes are automatically saved to `inventory.json`.

When the application starts, previously saved products are automatically loaded.

### ✅ Input Validation

The system checks for:

- Negative prices
- Negative quantities
- Duplicate Product IDs
- Invalid numeric input
- Non-existent Product IDs

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python 3 | Main programming language |
| JSON | Inventory data storage |
| `json` module | Reading and writing JSON data |
| `os` module | Checking whether the inventory file exists |
| OOP | Organizing products and inventory functionality |

---

## 📁 Project Structure

```text
Task 1/
│
├── Task 1.py
├── inventory.json
├── Readme.md
└── Screenshot.png
```

