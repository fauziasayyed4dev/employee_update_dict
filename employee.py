import sys

# Global list
employee_records = []

def AddEmployeeRecord():
    emp = dict()
    emp["name"] = input("Enter employee name: ")
    emp["id"] = int(input("Enter employee ID: "))
    emp["salary"] = float(input("Enter employee salary: "))
    emp["designation"] = input("Enter employee designation: ")
    employee_records.append(emp)
    print("Employee record added successfully.")

def ShowEmployeeRecords():
    if not employee_records:
        print("No employee records found.")
        return

    for emp in employee_records:
        print(f"Name: {emp['name']}")
        print(f"ID: {emp['id']}")
        print(f"Salary: {emp['salary']}")
        print(f"Designation: {emp['designation']}")
        print("-" * 20)

def DeleteEmployeeRecord(employee_id):
    for emp in employee_records:
        if emp["id"] == employee_id:
            employee_records.remove(emp)
            print(f"Employee record with ID {employee_id} deleted.")
            return
    print(f"No employee record found with ID {employee_id}.")

def UpdateEmployeeRecord(employee_id):
    for emp in employee_records:
        if emp["id"] == employee_id:
            #employee_records.update(emp)
            print("Employee found.Please update the new details")
             #emp = dict()
            emp["name"] = input("Enter new name: ")
            emp["salary"] = float(input("Enter new salary: "))
            emp["designation"] = input("Enter new designation:")
             # employee_records.append(emp)
            #print("Employee record added successfully.")
            print(f"Employee record with ID{employee_id} updated successfully")
            return
    print(f"No employee record found with ID you provided{employee_id}.")

def main():
    print("Employee Records Management System")

    choose = -1

    while choose != 0:
        print("\nMenu:")
        print("1. Add Employee Record")
        print("2. Show records")
        print("3. Delete Employee Record")
        print("4. Update Employee Record")
        print("0. Exit")
        choose = int(input("Choose an operation: "))

        if choose == 1:
            AddEmployeeRecord()
        elif choose == 2:
            ShowEmployeeRecords()
        elif choose == 3:
            employee_id = int(input("Enter employee ID to delete: "))
            DeleteEmployeeRecord(employee_id)
        elif choose == 4:
            employee_id = int(input("Enter employee ID to update: "))
            UpdateEmployeeRecord(employee_id)
        elif choose == 0:
            print("Exiting the program.")
        else:
            print("Invalid operation selected.")
        
    sys.exit(0)

# Correct entry point
if __name__ == "__main__":
    main()  