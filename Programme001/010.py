#Global Variables
calculation_to_units = 24
name_of_unit = "hours"

#Functions with local Variables
def days_to_units(num_of_days):
    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")

def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print  ("you have entered 0, please enter a valid positive number")
    else:
        print("Your input is not a valid number, stop breaking my programme")

#User input + Data Validation + output
user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")
validate_and_execute()
