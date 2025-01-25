
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

def display_employee(empname, hours, rate, gross, tax_rate, tax, net):
    print(f"\nEmployee name: {empname}")
    print(f"Hours worked: {hours}")
    print(f"Hourly rate: ${rate:.2f}")
    print(f"Gross pay: ${gross:.2f}")
    print(f"Income tax rate: {tax_rate:.1%}")
    print(f"Income tax: ${tax:.2f}")
    print(f"Net pay: ${net:.2f}")

def display_totals(num_employees, total_hours, total_gross, total_tax, total_net):
    print("\nPayroll Summary")
    print(f"Total employees: {num_employees}")
    print(f"Total hours: {total_hours}")
    print(f"Total gross pay: ${total_gross:.2f}")
    print(f"Total tax: ${total_tax:.2f}")
    print(f"Total net pay: ${total_net:.2f}")

def main():
    employees = 0
    total_hours = total_gross = total_tax = total_net = 0

    while True:
        empname = get_empname()
        if empname.lower() == "end":
            break

        hours = get_hours()
        rate = get_rate()
        tax_rate = get_tax_rate()

        gross, tax, net = calculate_pay(hours, rate, tax_rate)
        display_employee(empname, hours, rate, gross, tax_rate, tax, net)

        employees += 1
        total_hours += hours
        total_gross += gross
        total_tax += tax
        total_net += net

    display_totals(employees, total_hours, total_gross, total_tax, total_net)

if __name__ == "__main__":
    main()