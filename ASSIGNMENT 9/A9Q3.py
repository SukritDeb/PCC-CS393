f=open("ASSIGNMENT 9/files/A9Q3_file.txt","r")
text=f.read()
space=0
tab=0
newline=0
i=0
while(i<len(text)):
    #tab check is painful
    if(i+4<len(text) and text[i]==' ' and text[i+1]==' ' and text[i+2]==' ' and text[i+3]==' '):
        tab+=1
        i=i+4
    elif(text[i]=='\n'):
        newline+=1
        i=i+1
    elif(text[i]==' '):
        space+=1
        i=i+1
    else:
        i=i+1

print(f"No of spaces: {space} and No of tabs: {tab} and No of newlines: {newline}")
f.close()