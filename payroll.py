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

def write_employee_data(from_date, to_date, empname, hours, rate, tax_rate):
    with open("Employees.txt", "a") as file:
        file.write(f"{from_date}|{to_date}|{empname}|{hours}|{rate}|{tax_rate}\n")


def process_employee_data():

    try:
        with open("Employees.txt", "r") as file:
            records = file.readlines()
    except FileNotFoundError:
        print("No employee records found.")
        return
    
    while True:
        filter_date = input("Enter start date for report (MM/DD/YYYY) or 'All' to view all records: ")
        if filter_date.upper() == "ALL":
            filter_date = "ALL"
            break
        try:
            filter_date = datetime.strptime(filter_date, "%m/%d/%Y").strftime("%m/%d/%Y")
            break
        except ValueError:
            print("Invalid date format. Please enter in MM/DD/YYYY format.")
    
    totals = {
        'num_employees': 0,
        'total_hours': 0,
        'total_gross': 0,
        'total_tax': 0,
        'total_net': 0
    }
    
    print("\nEmployee Details:")
    print("-" * 60)

    details_printed = False
    
    for record in records:
        record = record.strip()
        from_date, to_date, name, hours, rate, tax_rate = record.split("|")
        hours, rate, tax_rate = float(hours), float(rate), float(tax_rate)

        # Filter records based on date
        if filter_date != "ALL" and from_date != filter_date:
            continue

        gross, tax, net = calculate_pay(hours, rate, tax_rate)
    
        print(from_date, to_date, name, f"{hours:,.2f}",  f"{rate:,.2f}", f"{gross:,.2f}",  f"{tax_rate:,.1%}",  f"{tax:,.2f}",  f"{net:,.2f}")
        
        # Update totals in dictionary
        totals['num_employees'] += 1
        totals['total_hours'] += hours
        totals['total_gross'] += gross
        totals['total_tax'] += tax
        totals['total_net'] += net
        details_printed = True

    if details_printed:
        display_totals(totals)
    else:
        print("\nNo matching records found.")
    

def display_totals(totals):
    print("\nPayroll Summary")
    print("-" * 80)
    print(f"Total employees: {totals['num_employees']}")
    print(f"Total hours: {totals['total_hours']}")
    print(f"Total gross pay: ${totals['total_gross']:.2f}")
    print(f"Total tax: ${totals['total_tax']:.2f}")
    print(f"Total net pay: ${totals['total_net']:.2f}")

def main():
    
    while True:
        empname = get_empname()
        if empname.lower() == "end":
            break
            
        from_date, to_date = get_work_dates()
        hours = get_hours()
        rate = get_rate()
        tax_rate = get_tax_rate()
        
        # Write employee data to file
        write_employee_data(from_date, to_date, empname, hours, rate, tax_rate)
        
    # Process employee data and get totals
    process_employee_data()

if __name__ == "__main__":
    main()