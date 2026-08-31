import random
random_number = random.randint(1,100)
number = 0

while number != random_number:
    try:
        number = int(input("enter a number"))
        if number > random_number:
            print("number is less")
        elif number < random_number:
            print("number is greater")
        else:
            print("you found the number")
    except ValueError:
        print("please type a number")