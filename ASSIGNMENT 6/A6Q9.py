def CustomCaesarCipher(message,key):
    if(key<0):
        return "Invalid Input"
    result=""
    for i in message:
        if(ord(i)>=65 and ord(i)<=90):
            # A TO Z
            count=ord(i)
            i=0
            while(i<key):
                if(count>=90):
                    count=64
                count=count+1
                i+=1
            result=result+chr(count)

        elif(ord(i)>=97 and ord(i)<=122):
            # a to z
            count=ord(i)
            i=0
            while(i<key):
                if(count>=122):
                    count=96
                count=count+1
                i+=1
            result=result+chr(count)

        elif(ord(i)>=48 and ord(i)<=57):
            #0 to 9
            count=ord(i)
            i=0
            while(i<key):
                if(count>=57):
                    count=47
                count=count+1
                i+=1
            result=result+chr(count)
        else:
            result=result+i
    return result
s=input("Enter your String: ")
n=int(input("Enter your key: "))
print(CustomCaesarCipher(s,n))