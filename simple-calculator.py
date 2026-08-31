number1 = None
number2 = None
while number1 == None or number2 == None:
    try:
        number1 = int(input("1st number"))
        number2 = int(input("2st number"))
    except ValueError:
        print("enter a number")

operators = ["+", "-", "*","/"]
selectoperator = ""
while selectoperator not in operators:
    selectoperator = str(input("enter operator + for addition, - for substration, * for multipication and / for division"))

match selectoperator:
    case "+":
        print(number1+number2)
    case "-":
        print(number1-number2)
    case "*":
        print(number1*number2)
    case "/":
        print(number1/number2)