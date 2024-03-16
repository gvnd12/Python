pb={}
while True:
    print("MENU")
    print("1.Add a contact")
    print("2.View contact")
    print("3.Update a contact")
    print("4.Delete a contact")
    print("5.Exit")
    choice=int(input("Enter your choice: "))

    if choice==1:
        c={}
        print("Add a contact")
        name=input("Enter name: ")
        email=input("Enter email: ")
        count=int(input("Enter count of phone numbers to be added: "))
        ph=[]
        for i in range(count):
            phno=input("Enter phone number: ")
            ph.append(phno)
        c['Name']=name
        c['Email']=email
        c['Phone number']=ph
        pb[name]=c
    elif choice==2:
        print("View contact")
        x=True
        while x==True:
            v=int(input("""Which contact do you want to view?:
                            1 -> All
                            2 -> Specific
                    """))
            if v==1:
                print(pb)
                x=False
            elif v==2:
                n=input("Enter the name of contact to be viewed: ")
                print(pb[n])
                x=False
            else:
                print("Invalid option")
    elif choice==3:
        print("Update a contact")
        u=input("Enter the name of contact to be updated: ")
        if u in pb:
            x=True
            while x==True:
                key=int(input("""Which detail need to be updated: 
                                1 -> Name
                                2 -> Email
                                3 -> Phone number
                        """))
                if key==1:
                    new_name=input("Enter new name: ")
                    pb[new_name]=pb.pop(u)
                    pb[new_name]['Name']=new_name
                    print("Update successful")
                elif key==2:
                    new_mail=input("Enter new email: ")
                    pb[u]['Email']=new_mail
                    print("Update successful")
                    x=False
                elif key==3:
                    p=input("Enter the phone number to be updated: ")
                    if p in pb[u]['Phone number']:
                        new_phno=input("Enter new phone number: ")
                    print("Update successful")
                    x=False
                else:
                    print("invalid option")
        else:
            print("Contact not found")
    elif choice==4:
        print("Delete a contact")
        del_name=input("Enter name of contact to be deleted: ")
        if del_name in pb:
            del pb[del_name]
            print("Contact of",del_name,"deleted")
        else:
            print("Contact not found")
    elif choice==5:
        print("Exiting the program")
        exit()
    else:
        print("Invalid choice")