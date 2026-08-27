import os 
import csv

student_data_path = "data.csv"

def load_students_data():
    if not os.path.exists(student_data_path) or os.path.getsize(student_data_path) == 0:
        return []
    students = []
    with open(student_data_path, mode = "r", newline = "", encoding = "utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            students.append(row)
    return students

def save_student_data(data):
    field_names = ["id", "name", "email", "age"]

    with open(student_data_path, mode = "w", newline = '', encoding = 'utf-8') as file:
        writer = csv.DictWriter(file, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(data)

    print("Successfuly added.....")
    
def add_new_student():
    students = load_students_data()
    if not students:
        id = 1
    else:
        last_student_id = students[-1]["id"]
        id = int(last_student_id) + 1

    print("--- ADD NEW STUDENT ---")
    print(f"Student id: {id:03d}")
    name = input("Name: ")
    email = input("Email: ")
    age = input("Age: ")    
    
    new_student = {
        "id": f"{id:03d}",
        "name": name,
        "email": email,
        "age": age
    }
    
    students.append(new_student)
    save_student_data(students)

def view_all_student():
    students = load_students_data()

    if not students:
        print("\nNo student register in system.")
        return
    print(f"{'=== STUDENTS LIST ===':^61}")
    print('-' * 62)
    print(f"| {'No.'}| {'ROLLNO':^8} | {'NAME':^10} | {'EMAIL':^20} | {'AGE':^7}|")
    print('-' * 62)
    i = 1
    for student in students:
        print(f"|{i:>2}. | {student.get("id"):^8} | {student.get("name"):<10} | {student.get("email"):<20} | {student.get("age"):^7}|")
        i += 1
    print('-' * 62)

def search_student():
    students = load_students_data()

    search_id = input("Enter student id: ")

    found_student = None
    for student in students:
        if search_id == student["id"]:
            found_student = student
            break
        
    if found_student:
        print("\n[+] Student Found!")
        print(f"ID    : {student["id"]}")
        print(f"Name  : {student["name"]}")
        print(f"Email : {student["email"]}")
        print(f"Age   : {student["age"]}")
    else:
        print(f"[!] Student not Found with ID {search_id}")

def update_student_record():
    students = load_students_data()
    student_id = input("Enter Student ID to update Record: ")

    found_student = None
    for student in students:
        if student_id == student["id"]:
            found_student = student
            break

    if found_student:
        print("\n[+] Student Found!")
        print(f"1. ID    : {found_student["id"]}")
        print(f"2. Name  : {found_student["name"]}")
        print(f"3. Email : {found_student["email"]}")
        print(f"4. Age   : {found_student["age"]}")
    else:
        print(f"[!] Student not Found with ID {student_id}")
        return
    
    field_to_update = int(input("Enter Field to Update (1-4): "))
    if field_to_update == 1: field_to_update = "id"
    elif field_to_update == 2: field_to_update = "name"
    elif field_to_update == 3: field_to_update = "email"
    elif field_to_update == 4: field_to_update = "age"
    else: 
        print("\n[!] Invalid option selected.\n") 
        return
    new_value = input(f"Enter new value for [{field_to_update}]: ").strip()

    if new_value:
        found_student[field_to_update] = new_value

        save_student_data(students)
        print("\n[+] Student record updated successfully!\n")
    else: 
        print("\n[!] Value cannot be empty. Update cancelled.\n")

def delete_student():
    students = load_students_data()
    student_id = input("Enter Student ID to delete: ").strip()

    found_student = None
    for student in students:
        if student_id == student["id"]:
            found_student = student
            break

    if found_student:
        students.remove(found_student)
        save_student_data(students)
        print(f"\n[+] Student with ID {student_id} ({found_student['name']}) has been deleted successfully!\n")
    else:
        print(f"\n[!] Student not found with ID: {student_id}\n")

def manu():
    print("=== WELCOME STUDENT RECORD SYSTEM ===")
    print("1. Add New Student")
    print("2. View All Sttudents")
    print("3. Search Student")
    print("4. Update Student Record")
    print("5. Delete Student")
    print("6. Exit")
    try:    
        option = int(input("Select Option (1-6): "))
        if option < 1 or option > 6:
            print("\n[!] Invalid choice. Please enter a number between 1 and 6.\n")
            return manu()
    except ValueError:
        print("\n[!] Invalid input! Please enter a valid number (1-6).\n")
        return manu()

    if option == 1:
        add_new_student()
        manu()
    elif option == 2:
        view_all_student()
        manu()
    elif option == 3:
        search_student()
        manu()
    elif option == 4:
        update_student_record()
        manu()
    elif option == 5:
        delete_student()
        manu()
    elif option == 6:
        exit

manu()