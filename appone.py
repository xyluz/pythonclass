name = input("What is your name? \n")

#allowedUsers = ['Seyi','Mike','Love']
#allowedPassword = ['passwordSeyi','passwordMike','passwordLove']

allowedUserDictionary = {
    'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
    }

if(name in allowedUserDictionary):
    password = input("Your password? \n")
    #userId = allowedUsers.index(name)

    if(password == allowedUserDictionary[name]):
        
        print('Welcome %s' % name)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))
        
        if(selectedOption == 1):
            print('you selected %s' % selectedOption)
            
        elif(selectedOption == 2):
            print('you selected %s' % selectedOption)
            
        elif(selectedOption == 3):
            print('you selected %s' % selectedOption)
            
        else:
            print('Invalid Option selected, please try again')
    
        
        
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')







