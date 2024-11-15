super_ascii=True
def getAscii(c):
    return ord(c)-96
s=input("Enter the string: ")
s=s.lower()
for i in s:
    if (i==" "):
        continue
    elif(getAscii(i)!=s.count(i)):

        super_ascii=False
if(super_ascii):
    print("Yes its super ASCII")
else:
    print("No its not a super ASCII")

