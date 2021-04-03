database_user = {
   'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
}

def login():
    #login function here
    name = input("What is your name? \n")
    password = input("Your password? \n")
    if(name in database_user and password == database_user[name]):
        print("Welcome " + name)
        return True
    else:
        print("Password or Username Incorrect. Please try again")
        return False


def bankOperations():
    
    print('These are the available options:')
    print('1. Withdrawal')
    print('2. Cash Deposit')
    print('3. Complaint')
    print('4. Logout')

    selectedOption = int(input('Please select an option:'))
            
    if(selectedOption == 1):
        print('you selected %s' % selectedOption)
        bankOperations()
                
    elif(selectedOption == 2):
        print('you selected %s' % selectedOption)
        bankOperations()
                
    elif(selectedOption == 3):
        print('you selected %s' % selectedOption)
        bankOperations()

    elif(selectedOption == 4):
        exit()   
    else:
        print('Invalid Option selected, please try again')


print("Welcome, what would you like to do?")
print("1. Login")
print("2. Register")

actionSelect = int(input("Select an option \n"))

if(actionSelect == 1):
    isLoginSuccessful = False

    while isLoginSuccessful == False:
        isLoginSuccessful = login()

    bankOperations()
            
else:
    print('Login failed, username or password incorrect')

    
        






























