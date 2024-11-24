def format_number(n):
    if(n<0):
        return;
    num=str(n)
    count=0
    result=""
    for i in range(len(num)-1,-1,-1):
        count=count+1
        if(count%3==0):
            result=result+num[i]+','
        else:
            result=result+num[i]
    return result[::-1]
print(format_number(1254789659595))
