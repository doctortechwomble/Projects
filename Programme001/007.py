#Global Variables
calculation_to_units = 24
name_of_unit = "hours"

#Functions with local Variables
def days_to_units(num_of_days):
    if num_of_days > 0:
        return (f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    elif num_of_days == 0:
        return "you have entered 0, please enter a valid positive number"
    else:
        return "you a entered a negative value, please try again"

#User input
user_input = input("Hey user, enter a number of days and I will convert it to hours!\n")

#convert user input from string to number
user_input_number = int(user_input)

#function using user input agaist calculation function
calculated_value = days_to_units(user_input_number)

#Outputs result
print(calculated_value)
