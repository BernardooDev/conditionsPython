calculation_to_seconds = 24 
hours = "hours"


def function_to_calculation(number_of_days):
    if number_of_days > 0:
        return f"{number_of_days} days is {number_of_days * calculation_to_seconds} {hours}"
    elif number_of_days = 0:
        return "0 days have 0 hours"
    else:
        return "you have to enter a positive number"

user_input = input("enter a number of day for a can convert in hours for you\n")

resultofinput = function_to_calculation(int(user_input))
print(resultofinput)