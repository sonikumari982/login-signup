print("'WECOME' to wold of accentuar")
print("login/singup")
option=input("enter hare whot you whant ")
if option=="singup":
    global name
    name=input("enter your name\n")
    print("here i wont your bio.data")
    hoby=input("what is your hobby\n")
    food=input("what is your favorat food\n")
    work=input("what are you doing your free time\n")
    date=input("date of biarth\n")
    i=0
    while i<100:
        print("password shoud be five digit")
        global p
        p=int(input("create your password"))
        forlen=str(p)
        if len(forlen)==5:
            if p>0 and p<=99999:
                print("password strong")
                break
            else:
                print("password not strong")
                print("create again")
        else:
            print(" not five digit password ")
            print("create again")
        
        i+=1
    # con=input("conform password")
    j=0
    while j<100:
        con=int(input("conform password"))
        if con==p:
            print("correct")
            break
        else:
            print("not match")
        j+=1
    link=input("whant to link with a facebook\nyes or no")
    if link=="yes":
        print(" link succesfull")
    else:
        print("not link")
log=input("do you whant to login \n yes or no")
if log=="yes":
    h=0
    while h<100:
        name2=input("enter name")
        if name2==name:
            print("correct")
            break
        else:
            print("enter the same 'name'whitch you use for singup")
        h+=1
    print("whitch you alrady creat")
    logpass=input("enter password")
    k=0
    while k<100:
        if logpass==p:
            print("correct")
            break
        else:
            print("not correct")
        k+=1
# else:
#     print('"WELCOME"\ncreating account is succesfill ')
print('"WELCOME"\ncreating account is succesfill ')
        