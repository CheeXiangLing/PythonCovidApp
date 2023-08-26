def signUp():
    print()
    print("Please register your info(^^__^^)")
    name=input("Please enter your name:")
    age=input("Please enter your age:")
    address=input("Please enter your home address:")
    postcode=input("Please enter your home postcode:")
    password=input("Please enter your password:")
    if(int(age) >= 60):
        categories="Senior"
    else:
        categories="Junior"
    emplo=open("User.txt","a")
    emplo.write(name)
    emplo.write("\n")
    emplo.write(age)
    emplo.write("\n")
    emplo.write(address)
    emplo.write("\n")
    emplo.write(postcode)
    emplo.write("\n")
    emplo.write(categories)
    emplo.write("\n")
    emplo.write(password)
    emplo.write("\n")
    
    emplo.close()
    mainmenu()

def viewFile():
    with open("User.txt","r")as f:
       lines=f.readlines()
    count = 0
    for line in lines:
       count+=1

    num=int(count/6)
    user=[]
    user_list=[]
    with open("User.txt","r")as fa:
        for i in range(num):
            user.append(fa.readline().rstrip("\n"))
            user.append(fa.readline().rstrip("\n"))
            user.append(fa.readline().rstrip("\n"))
            user.append(fa.readline().rstrip("\n"))
            user.append(fa.readline().rstrip("\n"))
            user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
          #  user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
           # user.append(fa.readline().rstrip("\n"))
            user_list.append(user)
            user=[]
        print(user_list,"\n")
        
        return user_list

def login():
    user=[]
    count=0
    i=0
    with open("User.txt","r")as fa:
        lines=fa.readlines()
    for line in lines:
        count+=1
    name=input("Please enter your name:")
    password=input("Please enter your password:")
   
    while(True):
        if((lines[i].strip("\n")==name) and (lines[i+5].strip("\n")==password)):
            print("Name and password correct")
            break 
        else:
            i+=6
            if(i>=count): 
                print("Name or Password does not exist,Please enter its again!!!")
                login()
                return False
    # amother way 
    # while(True):
    #     if(lines[i].strip("\n")==name):
    #         print("name correct")
    #         if(lines[i+5].strip("\n")==password):
    #             print("Password correct")
    #             return False
    #         else:
    #             print("Please reenter")
    #             login()
    #     else:
    #         i+=6
    #         if(i>=count):
    #             print("Name does not exist")
    #             return False

    print("Login successfully")
    user_Menu()
    

            
def user_Menu():
    print("Hellooo User")  

def mainmenu():
    print("-------------------------------------")
    print("Welcome to Vaccination Registration")
    print("-------------------------------------")
    print("1: Sign Up")
    print("2: Login")
    print("3: Admin")
    print("4: view file")
    print("5: Log Out")
    print("-------------------------------------")
    option=input("Please enter your choice:")
    if option == "1":
        signUp()
    elif option == "2":
        login()
    elif option =="4":
        viewFile()
    

mainmenu()

