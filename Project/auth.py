import random
import validation
import database
from getpass import getpass


# import mimetypes
#
# from getpass import getpass

# user_db_path = 'data/user_record/'

# database = {}


def init():
    print("\nWelcome to PythonBank")
    have_account = int(input("Do you have account with us: (1) Yes (2) No \n"))
    if have_account == 1:
        login()
    elif have_account == 2:
        register()
    else:
        print("You have selected invalid option")
        init()


# def current_balance(args):
#     pass


def login():
    print("********** Login **********")
    account_number_from_user = int(input("What is your account number? \n"))
    is_valid_account_number = validation.account_number_validation(account_number_from_user)

    if is_valid_account_number:
        password = input("What is your password \n")
        user = database.authenticated_user(account_number_from_user, password)

        if user:
            bank_operation(user)

        print('Invalid account or password')
        login()

    else:
        print("Account Number Invalid: check that you have up to 10 digits and only integers")
        init()


def register():
    print("********** Register **********")
    email = input("What is your email address? \n")
    first_name = input("What is your first name? \n")
    last_name = input("What is your last name? \n")
    password = input("Create a password for yourself \n")

    user_account_number = generation_account_number()

    # balance = set_current_balance(user_details, balance)

    is_user_created = database.create(user_account_number, first_name, last_name, email, password)
    #
    user_details = (first_name, last_name, email, password, 0)
    database[user_account_number] = (first_name, last_name, email, password, 0)

    if is_user_created:
        print("Your account has been created")
        print(" === ==== ====== ==== ===")
        print(f'Your account number is {user_account_number}')
        print("Make sure you keep it safe")
        print(" === ==== ====== ==== ===")


        login()

    else:
        print("Something went wrong, please try again \n")
        init()
        # change to login

def user_balance(user_account_number, balance, user_details=None):
    user_details[4] = balance



def bank_operation(user_details):

    # get_current_balance(, balance)
    print(f'\nWelcome {user_details[0]} {user_details[1]}')
    print("How can I help you today? \nAvailable Services:")
    selected_option = int(
        input('(1) Withdrawal \n(2) Deposit \n(3) Complaint \n(4) Logout \n(5) Exit \nPlease select an option: '))
    if selected_option == 1:
        withdrawal_operation(user_details)
    elif selected_option == 2:
        deposit_operation(user_details)
    elif selected_option == 3:
        complaint_operation(user_details)
    elif selected_option == 4:
        logout()
    elif selected_option == 5:
        exit()
    else:
        print("Invalid option selected")
        bank_operation(user_details)
    # return user


# def current_balance(args):
#     pass


def withdrawal_operation(user_account_number, user_details, balance):
    # get_current_balance(user_details, balance)
    user_details[4] = int(user_details[4])
    balance = user_details[4]
    print("\nWithdrawal Menu")
    print(f'You would like to make a withdrawal \nIs that correct?')
    confirm_withdrawal = int(input('Press (1) for Yes (2) for No \n'))
    if confirm_withdrawal == 1:
        print(f'Your current balance is {balance}')
        withdrawal_amount = int(input('How much would you like to withdraw?: \n'))
        print(f'You have chosen to withdrawal ${withdrawal_amount}')
        database.update(user_account_number, balance)

        if balance < withdrawal_amount:
            print(f'Sorry, the requested transaction cannot be completed \n'
                  f'The amount you are seeking to withdrawal exceeds your current balance of ${balance} \n'
                  f'Please try your transaction again')
            withdrawal_operation(user_account_number, user_details, balance)
        else:
            balance = balance - withdrawal_amount
            print(f'Your remaining balance is ${balance} \nPlease take your cash \nHave a nice day!')

        init()

    elif confirm_withdrawal == 2:
        bank_operation(user_details)
    else:
        print('Invalid option selected, please try again')
        withdrawal_operation(user_account_number, user_details, balance)


def deposit_operation(user_account_number, user_details, balance):
    # get_current_balance(user_details, balance)
    user_details[4] = int(user_details[4])
    print("Deposit Menu")
    print('You would like to make a deposit \nIs that correct?')
    confirm_deposit = int(input('Press (1) for Yes (2) for No \n'))
    if confirm_deposit == 1:
        deposit_amount = int(input('How much would you like to deposit?:\n '))
        print(f'You have chosen to deposit ${deposit_amount}')
        user_details[4] = user_details[4] + deposit_amount
        print(f'Your current balance is ${user_details[4]} \nHave a nice day!')
        database.update(user_account_number, balance)
        init(user_account_number, user_details, balance)
    elif confirm_deposit == 2:
        bank_operation(user_account_number, user_details, balance)
    else:
        print('Invalid option selected, please try again')
        deposit_operation(user_account_number, user_details, balance)


def complaint_operation(user_details):
    print("Complaint Menu")
    print('You would like to make a complaint \nIs that correct?')
    confirm_complaint = int(input('Press (1) for Yes (2) for No \n'))
    if confirm_complaint == 1:
        customer_complaint = str(input('What issue would you like to report?: '))
        print(f'Thank you for contacting us {user_details[0]}nWe appreciate your feedback \nHave a nice day!')
        init()
    elif confirm_complaint == 2:
        bank_operation(user_details)
    else:
        print('Invalid option selected, please try again')
        complaint_operation(user_details)


def generation_account_number():
    return random.randrange(1111111111, 9999999999)

# def set_current_balance(user_details, balance):
#     user_details[4] = balance
#     return balance

# def get_current_balance(balance):
#     return balance



def logout():
    login()




init()
# user_details = (first_name, last_name, email, password, 0)
