todo_array = ["1st todo"]
menu = ""
while True:

        menu = int(input("enter 1 to view todo, 2 to add todo and 3 to remove todo"))

        if menu == 1:
            count = 1
            for item in todo_array:
                print(count,":",item)
                count= count+1

        elif menu == 2:
            todo_item = str(input("write in todo : "))
            todo_array.append(todo_item)

        elif menu == 3:
            count = 1
            for item in todo_array:
                print(count,":",item)
                count= count+1

            remove_input = int(input("enter a numbr to remove"))
            todo_array.pop(remove_input-1)
            print(todo_array)