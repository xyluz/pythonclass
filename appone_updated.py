def bankOperations():

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

def withdrawal():
    
    amount = float(input("How much would you like to withdrawal?")
    print('processing..')
    print('take your cash')               
    
    
                   

name = input("What is your name? \n")

allowedUserDictionary = {
    'Seyi':'passwordSeyi',
    'Mike':'passwordMike',
    'Love':'passwordLove'
    }

if(name in allowedUserDictionary):
    password = input("Your password? \n")    

    if(password == allowedUserDictionary[name]):
        
        print('Welcome %s' % name)
        bankOperations()    
        
        
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')







