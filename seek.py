f=open("seek.txt","r+")
f.write("jian from manipur")
f.seek(4)
d=f.read()
print(d)
f.close()

