filename = 'timesheets.txt'

# 1. The Extraction & Cleaning Function
def load_timesheets(filename):
    employee_data = []
    with open(filename, 'r') as file:
        for line in file:
            parts = line.strip().split(',')

            if len(parts) == 4:
                try:
                    name = parts[0].strip()
                    dept = parts[1].strip()
                    rate = float(parts[2].strip())
                    hours = float(parts[3].strip())
                    
                    # Boss Level Challenge: Check for negative hours
                    if hours < 0:
                        print(f"Error: {name} has negative hours ({hours}). Skipping.")

                    employee_data.append({
                        'name': name,
                        'dept': dept,
                        'rate': rate,
                        'hours': hours
                    })
                except ValueError:
                    print(f"Warning: Skipping invalid data for {parts[0].strip()}")
    return employee_data



# 2. The Business Logic Function
def calculate_pay(rate, hours):
    if hours <= 40:
        return rate * hours
    else:
        overtime_hours = hours - 40
        return (rate * 40) + (overtime_hours * rate * 1.5)
    


# 3. The grouping function
def group_by_dept(employee_data):
    dept_groups = {}
    for emp in employee_data:
        payout = calculate_pay(emp['rate'], emp['hours'])
        dept = emp['dept']
        formatted_entry = f"{emp['name']}: ${payout:,.2f}"

        if dept not in dept_groups:
            dept_groups[dept] = []

        dept_groups[dept].append(formatted_entry)
    return dept_groups


# 4. The Execution Block
if __name__ == "__main__":
    data = load_timesheets(filename)
    grouped_data = group_by_dept(data)

    with open('payroll_report.txt', 'w') as report:
        for dept, employees in grouped_data.items():
            report.write(f"Department: {dept}\n")
            total_dept_cost = 0

            for emp_string in employees:
                report.write(f"  {emp_string}\n")

                cost = float(emp_string.split('$')[1].replace(',', ''))
                total_dept_cost += cost

            report.write(f"Total Department Cost: ${total_dept_cost:.2f}\n")
            report.write("-" * 30 + "\n")