from CRD import DataStore


if __name__=="__main__":
    print("1)Provide Filepath 2)Default Filepath(CWD)")
    try:
        n=int(input())
    except Exception as e:
        print(e)
    if n==1:
        f=input("Enter Filepath:")
        d = DataStore(f)
    if n==2:
        d=DataStore()
    else:
        print("Enter Correct option")
        exit()
    print("1)Create 2)Read 3)Delete ")
    print("Enter Exit to leave ")
    d = {"1": d.create, "2": d.read, "3": d.delete}
    while (True):
        l = input()
        if l not in d and l != "exit":
            print("Enter correct input")
            continue
        if l == "exit":
            break
        if l=="1":
            key=input("Enter Key:")
            value=input("Enter Value in Json:")
            time=(input("Enter Time:"))
            if time!="":
                print(d[l](key,value,int(time)))
            else:
                print(d[l](key,value))
        if l=="2" or l=="3":
            key = input("Enter Key:")
            print(d[l](key))



