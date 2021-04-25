import random
customer_database = {}
def init():
    print("Welcome to Pak Bank!")
    from datetime import datetime
    today = datetime.today() 
def login():
print('Welcome,what would you like to select?')
print("1, login")
print("2, register")
actionselect = int(input("Select an option \n"))
if(actionselect == 1):
            isLoginSuccessful == False
            while isLoginSuccessful == False:
                 isLoginSuccessful = Login()
            bankOperations()
else:
    print('Invalid Option Selected, please try again')
    if (account_number == 1):
        login()
    elif(account_number == 2):
            register()
    else:
        print("invalid selection")
init()

def register():
	  print('Create your unique bank account with us. \n')
	  email = input('What is your email address? \n')
	  global first_name
	  first_name = input('What is your first name? \n')
	  global last_name
	  last_name = input('What is your last name? \n')
	  password = input('Create your unique password. \n')
	

	  account_number = account_number_generator()
	

	  user_details = [email, first_name, last_name, password]
	

	
	  customers_database[account_number] = [first_name, last_name, email, password]
	

	  print('Your account has been created.')
	  print(' == ==== ==== ==== ==== ==== ==')
	  print('This is your account number: {account_number}')
	  print(' == ==== ==== ==== ==== ==== == ')
	  print('Make sure to keep it safe. \n')
	

	  login()
	

def login():
	  print('Login to your account. \n')
	  user_account_number = int(input('What is your account number? \n'))
	  password = input('What is your password? \n')
	

	  for account_number,user_details in customers_database.items():
	    if account_number == user_account_number:
	      if user_details[3] == password:
	        bank_operations(user_details)
	

	  print('Invalid account number or password')
	  login()
	

def bank_operations(user):
	print('Dear {first_name} {last_name}. \n')
print('These are the options available: ')
print('1, withdraw')
print('2, Cash deposit')
print('3, complaint')
choice = int(input('Select Option: '))
if choice == 1:
            pay = int(input('How much would you like to withdraw?: '))
            print("take your cash: " + str(pay))

elif choice == 2:
            collect = int(input('How much would you like to deposit?: '))
            print('Balance is: '+ str(collect))

elif choice == 3:
            complaint = str(input('What issue will you like to report?: '))
            print("Thank you for contacting us")
else:
            print('Invalid Option Selected, please try again')

def account_number_generator():
  return random.randrange(1000111111,9999999999)


def logout():
  login()


init()


