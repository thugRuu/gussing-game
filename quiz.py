questios =[{'question':"this is the first question","answer":{"1":"abc","2":"sve","3":"rrrt"},"correct":"abc"},
           {'question':"this is the second question","answer":{"1":"abc","2":"sve","3":"rrrt"},"correct":"abc"},
           {'question':"this is the third question","answer":{"1":"abc","2":"sve","3":"rrrt"},"correct":"abc"}]

score = 0



for question in questios:
    print(question["question"])
    answers = question["answer"]
    for key,value in answers.items():
        print(key,value)

    userinput = input("type 1 , 2 or 3")
    useranswer = question["answer"][userinput]
    if useranswer == question["correct"]:
        print("correct answer")
        score = score+1
            
    else:
        print("incorrect")

print("you got ",score, "score")
            