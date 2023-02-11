calculation_to_seconds = 24 
hours = "hours"


def function_to_calculation(number_of_days):
    return f"{number_of_days} dias são {number_of_days * calculation_to_seconds} {hours}"

user_input = input("enter a number of day for a can convert in hours for you\n")

user_input_int = int(user_input)

resultofinput = function_to_calculation(user_input_int)
print(resultofinput)