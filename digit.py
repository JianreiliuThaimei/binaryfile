fh=open("python.txt","r")
fw=open("python.txt","w")
rec=fh.read()
for a in rec:
    if (a.isdigit()!=True):
        print(a,end=" ") 
        fw.write(a)
fh.close()
fw.close()