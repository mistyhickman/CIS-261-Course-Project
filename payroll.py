
# make a function to mak sure all number values are pos
def check_user_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value < = 0:
                print("You must enter a positive number")
                continue
            return value
        except ValueError:
            print("Your input was invalid. Please enter a number.")


