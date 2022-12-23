def signup():
    user=input("enter username here")
    password=input("enter password here")
    file=open("details.txt", "a")
    file.write(f"{user},{password}\n")
    file.close()
    print("--------------------------")
    print("account created succesfully")
    print("--------------------------")


def login():
    user=input("enter username here")
    password=input("enter password here")
    file=open("details.txt", "r")
    records=file.readlines()
    flag=0
    for i in records:
        u,p=i.split(",")
        if user==u:
            flag=1
            if password+"\n"==p:
                print("---------------")
                print("login succesful")
                print("---------------")
            else:
                print("------------------")
                print("incorrect password")
                print("------------------")
    if flag==0:
        print("-----------------")
        print("invalid username")
        print("-----------------")

while True:
    print("**************************")
    print("Tanish authentication app")
    print("**************************")
    print("1-signup")
    print("2-login")
    print("3-exit program")
    print("----------------------")
    option=input("enter option number here: ")
    print("----------------------")
    if option=="1":
        signup()
    elif option=="2":
        login()
    elif option=="3":
        print("thank you")
        break
    else:
        print("invalid input")