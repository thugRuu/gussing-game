array = [{"type":"food","spent":1000}]

while True:
    print("press 1 to view")
    print("press 2 to add")
    print("press 3 to filter")


    userInput = int(input("enter 1, 2 or 3"))

    if userInput == 1:
        for items in array:
            print(items["type"])
            print(items["spent"])

    elif userInput == 2:
        print("put in the type of expense")
        exp_type = input()
        print("put in the spent of expense")
        exp_spent = input()
        array.append({"type":exp_type,"spent":exp_spent})

    elif userInput == 3:
        print("seart expence type")
        expenseType = input()
        filtered_data = [x for x in array if x["type"]== expenseType]
        print(filtered_data)
           
