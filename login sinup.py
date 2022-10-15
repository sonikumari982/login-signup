import json
print("\n 'click login if you already signup \n otherwise first click signup \n")

user=input('enter login or signup:-')
if user=='signup':
    name=input('enter your name:-')
    password1=input('enter your password:-')
    lower,upper,special,digit=0,0,0,0
    if len(password1)>=4:
            for i in password1:
                if(i.isupper()):
                    upper=1
                if (i.islower()):
                    lower=1
                if (i.isdigit()):
                    digit=1
                if '!' in password1 or '@' in password1 or '#' in password1 or '$' in password1 or '%' in password1 or '^' in password1 or'&' in password1:
                    special=1
            if (upper+lower+digit+special)!=4:
                print('\n                  creat a strong password\n password should be atleast one upper one lower one digit and one special character\n                  try later\n')
            else:
                password2=input('conform your password:-') 
                if password1!=password2:
                    print('both password is not same')
                else:
                    DOB=int(input('enter your date of birth:-'))
                    email=input('enter your email:-')
                    mobile=int(input('enter your mobile no:-'))
                    gender=input('enter your gender:-')
                    dic={}
                    dic['new']={}
                    dic['new']['name']=name
                    dic['new']['password']=password1
                    dic['new']['DOB']=DOB
                    dic['new']['email']=email
                    dic['new']['mobile']=mobile
                    dic['new']['gender']=gender
                    with open ('userdetails.json','w') as f:
                        a=json.dump(dic,f,indent=4)
                    print()   
                    print('congracts',name,'you sign up succesfully')
                

    else:
        print('password should be greater then 4')
   
elif user=='login':
    d=open('userdetails.json','r')
    h=json.load(d)
    name1=input('enter your name:-')
    if h['new']['name']== name1:
        password1=input('enter your password:-')
        if h['new']['password']==password1:
            print('you login successfully')
        else:
            print('password is not  same as the signup please try again')
    else:
        print('name is not  be same as the signup try again')

else:
    print("\nplease choose login or signup \n")
