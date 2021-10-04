#Functions
calculation_to_units = 24
name_of_unit = "hours"


def days_to_units():
    print(f"20 days are {20 * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units()

#Adding a function parameter)
def days_to_units(num_of_days):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print("All good!")

days_to_units(20)
days_to_units(35)
days_to_units(50)
days_to_units(110)

#Adding a function parameter)
def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}")
    print(custom_message)

days_to_units(20, "Awesome!")
