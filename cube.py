def cube(number) :
    return number * number * number

def divisible(number):
    if number % 3 == 0 :
        print(cube(number))
    
    else :
        print("Try again ")

num = int(input("Enter a number : "))
divisible(num)