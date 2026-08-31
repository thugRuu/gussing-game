import random

array = ["s","p","r"]
randommove = random.randint(0,2)
computermove = array[randommove]
user = ""

while user not in ["s","p","r"]:
    user = str(input("input s for scissor, p for paper and r for rock: "))


print("computer choosed : ", computermove)

if (user == computermove):
    print("draw")
elif(user == "s" and computermove == "p" ):
    print("you win")
elif(user == "p" and computermove == "s"):
    print("you loose")
elif(user=="r" and computermove == "s"):
    print("you win")
elif(user=="s" and computermove == "r"):
    print("you loose")
elif(user=="p" and computermove == "r"):
    print("you win")
elif(user=="r" and computermove == "p"):
    print("you loose")
