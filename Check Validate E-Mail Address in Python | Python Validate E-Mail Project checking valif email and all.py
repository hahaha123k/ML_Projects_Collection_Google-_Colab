#Check Validate E-Mail Address in Python | Python Validate E-Mail Project.


email=input("Enter Your Email: ")#g@g.in,g@g.com
j,k,d=0,0,0;
if len(email)>=6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@")==1):
            if (email[-4]==".") ^ (email[-3]=="."):
                for i in email :
                    if i==i.isspace():
                        k=1
                    elif i.isalpha():
                        if i==i.upper():
                            j=1
                    elif i.isdigit():
                        continue
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        d=1
                if k==1 or j==1 or d==1:
                  print("Invalid Email 6")      
                else:
                    print("Valid Email 5")
            else:
                print("Invalid Email 4")
        else:
            print("Invalid Email 3")
    else:
        print("Invalid Email 2")
else:
    print("Invalid Email 1")
