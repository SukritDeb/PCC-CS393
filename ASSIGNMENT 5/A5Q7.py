sampleDict={"a":100,"b":200,"c":300}
n=int(input("Enter your input number: "))
if(n in sampleDict.values()):
    print(f"{n} exists in the dictionary..")
else:
    print(f"{n} does not exist in the dictionary..")