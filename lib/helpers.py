from models.department import Department
from models.employee import Employee


def exit_program():
    print("Goodbye!")
    exit()

# We'll implement the department functions in this lesson


def list_departments():
    departments = Department.get_all()
    for department in departments:
        print(department)


def find_department_by_name():
    name = input("Enter the department's name: ")
    department = Department.find_by_name(name)
    print(department) if department else print(
        f'Department {name} not found')


def find_department_by_id():
    # use a trailing underscore not to override the built-in id function
    id_ = input("Enter the department's id: ")
    department = Department.find_by_id(id_)
    print(department) if department else print(f'Department {id_} not found')


def create_department():
    name = input("Enter the department's name: ")
    location = input("Enter the department's location: ")
    try:
        department = Department.create(name, location)
        print(f'Success: {department}')
    except Exception as exc:
        print("Error creating department: ", exc)


def update_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        try:
            name = input("Enter the department's new name: ")
            department.name = name
            location = input("Enter the department's new location: ")
            department.location = location

            department.update()
            print(f'Success: {department}')
        except Exception as exc:
            print("Error updating department: ", exc)
    else:
        print(f'Department {id_} not found')


def delete_department():
    id_ = input("Enter the department's id: ")
    if department := Department.find_by_id(id_):
        department.delete()
        print(f'Department {id_} deleted')
    else:
        print(f'Department {id_} not found')


# You'll implement the employee functions in the lab

def list_employees():
    employees = Employee.get_all()
    for employee in employees:
        print(employee)

def find_employee_by_name():
    name = input("Enter the employee's name: ")
    employees = Employee.find_by_name(name)
    print(employees) if employees else print(
        f'Employee {name} not found')

def find_employee_by_id():
    id_ = input("Enter the Employee's id: ")
    employee = Employee.find_by_id(id_)
    print(employee) if employee else print(f'Employee {id_} not found')

def create_employee():
    try:
        # Get employee info
        name = input("Enter the Employee's name: ")
        job_title = input("Enter the Employee's job title: ")
        
        # Show available departments
        print("\nAvailable Departments:")
        departments = Department.get_all()
        for dept in departments:
            print(f"{dept.id}: {dept.name}")
        
        # Get department ID
        department_id = int(input("\nEnter the Department ID: "))
        
        # Create employee
        employee = Employee.create(name, job_title, department_id)
        print(f'\nSuccess: {employee}')
    except ValueError as exc:
        print("Error creating employee: ", exc)

def update_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(int(id_)):  # Convert id to int
        try:
            # Get new name (or keep existing if empty)
            new_name = input(f"Enter new name (currently {employee.name}, press Enter to keep): ")
            if new_name.strip():
                employee.name = new_name

            # Get new job title (or keep existing if empty)
            new_job = input(f"Enter new job title (currently {employee.job_title}, press Enter to keep): ")
            if new_job.strip():
                employee.job_title = new_job

            # Show departments and get new department id (or keep existing if empty)
            print("\nAvailable Departments:")
            departments = Department.get_all()
            for dept in departments:
                print(f"{dept.id}: {dept.name}")
            new_dept = input(f"Enter new department ID (currently {employee.department_id}, press Enter to keep): ")
            if new_dept.strip():
                employee.department_id = int(new_dept)

            employee.update()
            print(f'\nSuccess: {employee}')

        except Exception as exc:
            print("Error updating employee: ", exc)
    else:
        print(f'Employee {id_} not found')

def delete_employee():
    id_ = input("Enter the employee's id: ")
    if employee := Employee.find_by_id(id_):
        employee.delete()
        print(f'Employee {id_} deleted')
    else:
        print(f'Employee {id_} not found')

def list_department_employees():
    print("\nAvailable Departments:")
    departments = Department.get_all()
    for dept in departments:
        print(f"{dept.id}: {dept.name}")
    
    dept_id = int(input("\nEnter department ID to list employees: "))
    
    employees = Employee.get_all()
    
    dept_employees = [employee for employee in employees if employee.department_id == dept_id]
    
    if dept_employees:
        print(f"\nEmployees in department {dept_id}:")
        for employee in dept_employees:
            print(f"- {employee.name}: {employee.job_title}")
    else:
        print(f"\nNo employees found in department {dept_id}")