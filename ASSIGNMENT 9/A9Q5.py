print("Quiz Competition")
f=open("./files/A9Q5_ques.txt","r")
f2=open("./files/A9Q5_ans.txt","r")
while(True):
    ques=f.readline()
    if not ques:
        break
    ans=f2.readline()
    if not ans:
        break
    print(ques)
    choice=input("Want to see the answer: (y/n): ")
    if(choice=="y"):
        print(ans)
    choice2=input("Want to see the next question: (y/n): ")
    if(choice2=="n"):
        print("Thank you")
        break
    else:
        continue