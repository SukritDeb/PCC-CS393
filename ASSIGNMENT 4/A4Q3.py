str_list=eval(input("Enter the list of strings: "))
if(len(str_list)!=0):
    max=len(str_list[0])
    for i in str_list:
        if(len(i)>max):
            max=len(i)
print(max)