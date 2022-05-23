import pickle
def write():
    f=open("studentDetails.dat","wb")
    while True:
        roll=int(input("enter the roll no:-"))
        name=input("enter the name:-")
        data=[roll,name]
        pickle.dump(data,f)
        choice=input("more?(Y/N)")
        if choice in "Nn":
            break
    f.close()
def read():
    f=open("studentDetails.dat","rb")
    try:
        while True:
            r=pickle.load(f)
            print(r)
    except EOFError:
        f,close()
def search():
    found=0
    rollno=int(input("enter the rollno whose name you want to display:-"))
    f=open("studentDetails.dat","rb")
    try:
        while True:
            r=pickle.load(f)
            if r[0]==rollno:
                print(r[i])
                found=1
                break
    except EOFError:
        f.close()
    if found==0:
        print("sorry record not found")
write()
search()