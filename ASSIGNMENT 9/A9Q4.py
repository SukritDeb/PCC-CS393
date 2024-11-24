f=open("A9Q4_file.txt","r")
text=f.read()
linelist=text.split('\n')
l=[]
for i in linelist:
    l.append(0)
for i in range (len(linelist)):
    j=linelist[i]
    l[int(j[0])-1]=linelist[i]
f.close()
f2=open("A904_outputfile.txt","w")
for i in l:
    f2.write(str(i))
    f2.write('\n')
f2.close()
