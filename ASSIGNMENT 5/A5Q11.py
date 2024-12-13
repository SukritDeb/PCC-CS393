def sum_positive(*args):
    sum=0
    for i in args:
        if(i>0):
            sum=sum+i
    return sum
print(sum_positive(-1,5,8,9,-5,-8))