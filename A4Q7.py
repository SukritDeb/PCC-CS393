list1=eval(input("Enter the first list: "))
list2=eval(input("Enter the second list: "))
if(len(list1)==len(list2)):
    for i in range(len(list1)):
        if(list1[i]!=list2[i]):
            print(i)
            break;