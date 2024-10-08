def factorial(number):
    '''This is a function to find the factorial'''
    if number == 0 or number == 1:
        return 1
    else:
        return(number * factorial(number - 1))

print(factorial.__doc__)
print(factorial(10))