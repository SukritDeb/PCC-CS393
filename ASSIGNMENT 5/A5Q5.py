keys=["Ten","Twenty","Thirty"]
values=[10,20,30]
dic={}
for i in range(len(keys)):
    dic.update({keys[i]:values[i]})
print(dic)