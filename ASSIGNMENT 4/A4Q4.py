num=eval(input("Enter the numerator: "))
deno=eval(input("Enter the denominator: "))
result=[]
if(len(num)==len(deno)):
    for i in range(len(num)):
        result.append(num[i]/deno[i])
min=min(result)
i=result.index(min)
print(f"Minimum fraction is: {num[i]}/{deno[i]}")