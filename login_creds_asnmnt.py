# -*- coding: utf-8 -*-
"""
Created on Thu Jul 28 17:43:01 2022
# Id validation=([a-z]{1,})[0-9]{1,}[@]([a-z]{2,})([.][a-z]{2,})
@author: Sundar
"""

import re
def registration():
    
    f= open("creds file.txt","r")
    uid=[]
    upwd=[]
    for i in f:
        splitted_i=i.split(",")
        k=(splitted_i[0])
        v=(splitted_i[-1].strip("\n"))
        uid.append(k)
        upwd.append(v)   
    user_id=input("Create User ID : ")
    if user_id in uid:
        print("ID exists,try new ID")
        registration()
    else:
        regex=r"(([a-z]{1,})[a-z0-9]{1,}[@]([a-z]{2,})([.][a-z]{2,}))"
        match=re.search(regex,user_id)
        if match!=None:
            print("ID validation success") 
        #password validation
            user_pwd=input("Create password : ")
            regex=r"((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W])([\w\W]{5,16}))"
            match=re.search(regex,user_pwd)
            if match!=None:
                print("Password validation success")
                login()
                f= open("creds file.txt","a")
                f.write(user_id+","+user_pwd+"\n") 
            else:
                print(" password requirement unmet, Enter a valid password")
                registration() 
        else:
            print("Enter a valid ID")
            registration()               
    f.close()  

def reset_pwd():
    import re
    f= open("creds file.txt","r")
    uid=[]
    upwd=[]
    for i in f:
        splitted_i=i.split(",")
        k=(splitted_i[0])
        v=(splitted_i[-1].strip("\n"))
        uid.append(k)
        upwd.append(v)         
    user_id=input("Enter User ID : ")
    if user_id in uid:
        user_pwd=(input("enter new password : "))
        regex=r"((?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W])([\w\W]{5,16}))"
        match=re.search(regex,user_pwd)
        if match!=None:
            print("Password validation success")            
            for i in range(len(uid)):                
                if user_id==uid[i]:                  
                    user_detail= user_id+","+user_pwd+"\n"                                        
                    f=open("creds file.txt")
                    list_of_str=f.readlines()                    
                    list_of_str[i]=user_detail
                    f=open("creds file.txt","w")
                    replacement="".join(list_of_str)
                    f.write(replacement)
                    f.close()                                    
            print("Your password has been successfully reset")
            login() 
        else:
            print(" password requirement unmet, Enter a valid password")
            reset_pwd()
        
def login():    
    f= open("creds file.txt","r")
    uid=[]
    upwd=[]
    for i in f:
        splitted_i=i.split(",")
        k=(splitted_i[0])
        v=(splitted_i[-1].strip("\n"))
        uid.append(k)
        upwd.append(v)        
    user_id=(input("Enter User id : "))
    if user_id in uid:
        user_pwd=(input("Enter password : "))
        uid_ind=uid.index(user_id)
        if user_pwd==upwd[uid_ind]:
            print("login success")
        else:
            choice=input(('''incorrect password,
type 'try again' or 'reset password' or 'forgot password' : ''').lower())
            if choice=="try again":
                login()                        
            elif choice=="reset password":
                reset_pwd()
            elif choice=="forgot password":
                id_=input("Enter user id : ")
                if id_ in uid:
                    uid_ind=uid.index(user_id)
                    print("your password is :",upwd[uid_ind])
                else:
                    choice=input(('''Enter a valid response,
type 'try again' or 'reset password' or 'forgot password' : ''').lower())    
    else:
        print("Incorrect user id, try again")
        login()                     
    f.close()
    
def home_screen():
    print('''
          ====================
          |      Hola        |
          ====================
           ''')
    user_input=input("Do you wish to Login | Register : ").capitalize()
    if user_input=="Login":
        login()
    elif user_input=="Register":
        registration()
    else:
        print("Enter a valid response")
        home_screen()
home_screen()
        
