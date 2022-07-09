password = input("Create password ")
pass_key = "password"
if input("What is your password? ") == password:
    pass_key = password
while pass_key != password:
    print("wrong password!")
    pass_key = input("What is your password? ")
    
while pass_key == password:
    command1 = input("Enter your command to open, close or quit ")
    if command1 == "open":
        print("The door is now open")
        command2 = input("Enter your command to open, close or quit ")
        if command2 == command1:
            print("The door is already open")
    if command1 == "close":
        print("The door is now locked")
        command2 = input("Enter your command to open, close or quit ")
        if command2 == "open":
            print("The door is already locked")
    

    if command1 == "quit":
        quit()
