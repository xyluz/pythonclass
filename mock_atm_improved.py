import datetime
import random

beginning_balance = 200

database = {}

def generated_account_number():
    return random.randrange(1111111111,9999999999)

account_number = generated_account_number()


def login():
    print("********** Login **********")
    account_number_from_user = int(input("What is your account number? \n"))
    password = input("What is your password \n")

    for account_number,user_details in database.items():
        if(account_number == account_number_from_user):
            if(user_details[3] == password):
                bank_operation(user_details)
            break
    else:
        print('Invalid username or password')
        init()

def register():
    print("********** Register **********")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n") 
    
    account_number = generated_account_number()
    database[account_number] = [first_name, last_name, email, password]
    
    print("Your account has been created")
    print(" === ==== ====== ==== ===")
    print(f'Your account number is {account_number}')
    print("Make sure you keep it safe")
    print(" === ==== ====== ==== ===")
    
    login()


def init():
    print("\nWelcome to PythonBank")
    have_account = int(input("Do you have account with us: (1) Yes (2)No \n"))
    if(have_account == 1):
        login()
    elif(have_account == 2):
        register()
    else:
        print("You have selected invalid option")
        init()
    

def bank_operation(user):
    print(f'\nHello {user[0]} {user[1]}')
    print("How can I help you today? \nAvailable Services:")
    selected_option = int(input('(1) Withdrawl \n(2) Deposit \n(3) Complaint \n(4) Logout \n(5) Exit \nPlease select an option: '))
    if selected_option == 1:
        withdrawal_operation(user)
    elif selected_option == 2:
        deposit_operation(user)
    elif selected_option == 3:
        complaint_operation(user)
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user)
    return user

        
def withdrawal_operation(user):
    print("\nWithdrawal Menu")
    print(f'You would like to make a withdrawl \nIs that correct?')
    confirm_withdrawl = int(input('Press (1) for Yes (2) for No \n'))    
    if confirm_withdrawl == 1:
        withdrawl_amount = int(input('How much would you like to withdraw?: \n'))
        print(f'You have chosen to withdrawl ${withdrawl_amount} \nPlease take your cash \nHave a nice day!')
        init()
    elif confirm_withdrawl == 2:
        bank_operation(user)
    else:
        print('Invalid option selected, please try again')
        withdrawal_operation(user)

def deposit_operation(user):
    print("Deposit Menu")
    print('You would like to make a deposit \nIs that correct?')
    confirm_deposit = int(input('Press (1) for Yes (2) for No \n'))    
    if confirm_deposit == 1:
        deposit_amount = int(input('How much would you like to withdraw?:\n '))
        print(f'You have chosen to deposit ${deposit_amount}')
        current_balance = deposit_amount + beginning_balance    
        print(f'Your current balance is ${current_balance} \nHave a nice day!')
        init()
    elif confirm_deposit == 2:
        bank_operation(user)   
    else:
        print('Invalid option selected, please try again')
        deposit_operation(user)

def complaint_operation(user):
    print("Complaint Menu")
    print('You would like to make a complaint \nIs that correct?')
    confirm_complaint = int(input('Press (1) for Yes (2) for No \n'))     
    if confirm_complaint == 1:
        customer_complaint = str(input('What issue would you like to report?: '))
        print(f'Thank you for contacting us \nWe appriciate your feedback \nHave a nice day!')
        init()
    elif confirm_complaint == 2:
     bank_operation(user)   
    else:
        print('Invalid option selected, please try again')
        complaint_operation(user)

def logout():
    login()

def exit():
    init()


init()
                
