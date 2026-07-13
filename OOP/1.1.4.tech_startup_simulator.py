# Phase 1: The Blueprints (OOP & inheritance)
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def get_details(self):
        return f"Name: {self.name}, Salary: ${self.base_salary}"
    
class Developer(Employee):
    def __init__(self, name, base_salary, programming_language):
        super().__init__(name, base_salary)
        self.programming_language = programming_language

    def get_details(self):
        base_info = super().get_details()
        return f"{base_info}, Language: {self.programming_language}"
    
class Manager(Employee):
    def __init__(self, name, base_salary, department):
        super().__init__(name, base_salary)
        self.department = department

    def get_details(self):
        base_info = super().get_details()
        return f"{base_info}, Department: {self.department}"
    


# Phase 2: The Database (Data Structures & Composition)
class Company:
    def __init__(self):
        self.roster = []

    def hire_employee(self, employee_obj):
        self.roster.append(employee_obj)

    def show_roster(self):
        for employee in self.roster:
            print(employee.get_details())


    # Phase 3: Data Persistence (File Handling)
    def export_roster(self):
        with open("company_data.txt", "w") as file:
            for employee in self.roster:
                file.write(employee.get_details() + "\n")

        print("\nRoster exported to company_data.txt")


# Phase 4: The Interface (Loops & Conditionals)
my_startup = Company()

while True:
    print("\n--- Tech Startup Simulator ---")
    print("1. Hire Developer | 2. Hire Manager | 3. Show roster | 4. Export & Exit.")

    option = input("Select an option: ")
    if option == "1":
        name = input("Enter Developer name: ")
        salary = input("Enter salary: ")
        language = input("Enter programming language: ")
        dev = Developer(name, salary, language)
        my_startup.hire_employee(dev)
        print(f"{name} has been employed as a developer.")

    elif option == "2":
        name = input("Enter Manager name: ")
        salary = input("Enter salary: ")
        dept = input("Enter department: ")
        mgr = Manager(name, salary, dept)
        my_startup.hire_employee(mgr)
        print(f"{name} has been employed as a manager.")

    elif option == "3":
        print("\n--- Current Roster ---")
        my_startup.show_roster()

    elif option == "4":
        my_startup.export_roster()
        print("Exiting...")
        break

    else: 
        print("Invalid choice, please try again.")







