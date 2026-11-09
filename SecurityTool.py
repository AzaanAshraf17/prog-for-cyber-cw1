#will store the correct username and password details that are required to use security menu tool

correct_username = "admin"
correct_password = "pass123"

#user must authenticate before being able to use the security menu tool
username = input("Enter the Username: ")
password = input("Enter the password: ")

# the while loop will ask the user until the correct password a username are enterted
while username != correct_username or password != correct_password:
    print("incorrect username or password please try again")
    username = input("Enter the Username: ")
    password = input("Enter the password: ")

print("Authentication was sucessful, welcome to the security tool")

# the secuirty tool menu

choice = 0

#the while loop will display the menu till user exits the menu
while choice != 4:

    print("\n Security tools menu")
    print("1. Security Event Counter")
    print("2 Brute force Simulation")
    print("3 Login Authetication")
    print("4 Exit")

    choice = int(input("Enter your choice:"))

    #option 1 security event counter

    if choice == 1:

        correct = 0
        incorrect = 0

        #will ask the user for the password 10 times

        for i in range(10):

            guess = input("Enter the password:")

            if guess == password:
                correct += 1
            else:
                incorrect += 1

        percentage = incorrect * 10

        print("The Results are:")
        print("Correct:", correct)
        print("incorrect:", incorrect)
        print("incorrect percentage:", percentage)

        if percentage > 50:
            print("Alert: too many incorrect passwords")

    #option 2 Brute force simulation
    elif choice == 2:

    #number of attempts are at 0 
        attempts = 0
        guess = ""

        # while loop will allow user gets a  Max of 5 attempts
        while guess != password and attempts < 5:
            guess = input("Guess the password:")
             
            if guess != password:
                print("Password is incorrect please try again")
            
            attempts += 1
      
      #if user enters wrong the Max attempts are reached
        if guess == password:
            print("Correct password")
            print("Attempts:", attempts)
        else:
            print("Max attempts reached")

    #option 3 Login authentication
    elif choice == 3:

      #number of attempts are at 0
        attempts = 0

      # while loop will allow the user 3 attempts to log in
        while attempts < 3:

            user = input("Enter username:")
            pw = input("Enter password:")

          #checks if the details entered match the correct username and password
            if user == correct_username and pw == correct_password:
                print("Authentication sucessful")
                break
            else:
                print("Authentication failed")
                attempts += 1

      #locks the Account after 3 failed attempts to log in
        if attempts == 3:
            print("Account frozen for 24 hrs")

    #option 4 Exits Security tool menu and thanks user
    elif choice == 4:
        print("Thanks for using the security tool")

    #anything else that 1 - 4
    else:
        print("invalid option please enter a number between 1 and 4")
