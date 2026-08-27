# Student Record System Documentation

## 1. Overview
This is a command-line Python application designed to manage student information stored in a CSV file (data.csv). It function (Add, Read, Update, Delete, Search) operations with automatic ID generation.

## 2. File Structure & Storage
`data.csv:` The backend storage file containing comma-separated fields: id, name, email, and age.

`load_students_data():` Checks if the CSV file exists and is non-empty, then loads all rows into a list of dictionaries using csv.DictReader.

`save_student_data(data):` Overwrites the CSV file with the updated list of dictionaries using csv.DictWriter and writes the header row.

## 3. Core Features & Functions
`add_new_student():` Automatically checks the last record's ID, increments it, pads it to 3 digits (e.g., 001, 017), and appends the new record.

`view_all_student():` Loads and renders all student records in a clean, formatted ASCII text table.

`search_student():` Prompts for a specific Student ID, performs an exact match search, and prints out the student details if found.

`update_student_record():` Locates a student by ID, lets the user choose a specific field (Name, Email, or Age) to update, and saves the changes.

`delete_student():` Finds a student record by ID and removes it entirely from the database.

`manu():` Controls the user interface loop, handles input errors gracefully, and routes choices to respective functions.