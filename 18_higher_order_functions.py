

def sum_one (value):
    return value + 1

def sum_five (value):
    return value + 5

def sum_two_values_and_one (first_value, second_value,f_sum):
    return f_sum (first_value + second_value)

print (sum_two_values_and_one(3,2,sum_one))
print (sum_two_values_and_one(3,2,sum_five))