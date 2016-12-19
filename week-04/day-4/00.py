def factorial(number):
    if number <= 1:         #base case
        return 1
    else:
        return number * factorial(number-1)

    # product = 1
    # for i in range(number):
    #     product = product * (i + 1)
    # return product

user_input = 6
factorial_of_input = factorial(user_input)
print(factorial_of_input)
