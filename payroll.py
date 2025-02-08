from datetime import datetime

def get_work_dates():
    while True:
        try:
            from_date = input("Enter from date (mm/dd/yyyy): ")
            to_date = input("Enter to date (mm/dd/yyyy): ")
            # Validate date format and convert to datetime objects
            from_date_obj = datetime.strptime(from_date, '%m/%d/%Y')
            to_date_obj = datetime.strptime(to_date, '%m/%d/%Y')
            # Return formatted dates with leading zeros
            return (from_date_obj.strftime('%m/%d/%Y'), 
                   to_date_obj.strftime('%m/%d/%Y'))
        except ValueError:
            print("Invalid date format. Please use mm/dd/yyyy")

def get_empname():
    return input("Enter employee name (or 'End' to finish): ")

def get_hours():
    while True:
        try:
            value = float(input("Enter hours worked: "))
            if value < 0:
                print("Please enter a number of hours worked.")
                continue
            return value
        except ValueError:
            print("You didn't enter a number. Please try again")

def get_rate():
    while True:
        try:
            value = float(input("Enter hourly rate: $"))
            if value < 0:
                print("Please enter a positive number for hourly rate.")
                continue
            return value
        except ValueError:
            print("You didn't enter a number. Please try again")

def get_tax_rate():
    while True:
        try:
            value = float(input("Enter tax rate (as decimal, e.g. 0.2 for 20%): "))
            if value < 0:
                print("Please enter a positive number for tax rate.")
                continue
            return value
        except ValueError:
            print("You didn't enter a number. Please try again")

def calculate_pay(hours, rate, tax_rate):
    gross = hours * rate
    tax = gross * tax_rate
    net = gross - tax
    return gross, tax, net

def process_employee_data(employee_data):
    totals = {
        'num_employees': 0,
        'total_hours': 0,
        'total_gross': 0,
        'total_tax': 0,
        'total_net': 0
    }
    
    print("\nEmployee Details:")
    print("-" * 60)
    
    for emp in employee_data:
        from_date, to_date, name, hours, rate, tax_rate = emp
        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        
        print(f"\nPay Period: {from_date} to {to_date}")
        print(f"Employee name: {name}")
        print(f"Hours worked: {hours}")
        print(f"Hourly rate: ${rate:.2f}")
        print(f"Gross pay: ${gross:.2f}")
        print(f"Income tax rate: {tax_rate:.1%}")
        print(f"Income tax: ${tax:.2f}")
        print(f"Net pay: ${net:.2f}")
        
        # Update totals in dictionary
        totals['num_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross'] += gross
        totals['total_tax'] += tax
        totals['total_net'] += net
    
    return totals

def display_totals(totals):
    print("\nPayroll Summary")
    print("-" * 80)
    print(f"Total employees: {totals['num_employees']}")
    print(f"Total hours: {totals['total_hours']}")
    print(f"Total gross pay: ${totals['total_gross']:.2f}")
    print(f"Total tax: ${totals['total_tax']:.2f}")
    print(f"Total net pay: ${totals['total_net']:.2f}")

def main():
    employee_data = []  # List to store employee information
    
    while True:
        empname = get_empname()
        if empname.lower() == "end":
            break
            
        from_date, to_date = get_work_dates()
        hours = get_hours()
        rate = get_rate()
        tax_rate = get_tax_rate()
        
        # Store employee data in list
        employee_data.append([from_date, to_date, empname, hours, rate, tax_rate])
        
    # Process employee data and get totals
    if employee_data:
        totals = process_employee_data(employee_data)
        display_totals(totals)
    else:
        print("Could not find any employees. I work better with actual data!")

if __name__ == "__main__":
    main()