import pickle
def write():
    f=open("studentDetails.dat","wb")
    while True:
        r=int(input("enter roll no:-"))
        n=input("enter the name:-")
        m=int(input("enter the mark:-"))
        record=[r,n,m]
        pickle.dump(record,f)
        ch=input("do you want to enter more records(Y/N)")
        if ch in "Nn":
            break
        f.close()
def read():
    f=open("studentDetails.dat","rb")
    try:
        while True:
            red=pickle.load(f)
        print(red)
    except EOFError:
        f.close()
def update():
    f=open("student.Details.dat","rb+")
    rollno=int(input("enter rollno whose mark to be update"))
    try:
        while True:
            pos=f.tell()
            red=pickel.load(f)
            if red[0]==rollno:
                an=int(input("enter the update"))
                red[2]==an
                f.seek(pos)
                pickle.dump(red,f)
                print(red)
    except EOFError:
        f.close()
write()
read()
update()
read()        
        
        