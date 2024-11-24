pangram=True
s=input("Enter the string: ")
s=s.lower()
for i in range(97,123):
    if(i==" "):
        continue
    elif(chr(i) not in s):
        pangram=False
if(pangram):
    print("yes it is pangram..")
else:
    print("No it is not pangram..")