import random

accountList = {}
accountDetails = []
total_balance = 0


def Begin():
    print("Welcome to ElenuBak")
    print("for new user press 1 to Register\nFor existing user press 2 to login")
    userOption = int(input("Select an option"))

    if userOption == 1:
        userRegistration()

    elif userOption == 2:
        userLogin()

    else:
        print("Invalid transaction")


def userLogin():
    print("Please enter your login Detail")
    userAccountNumber = int(input("please enter your account number : "))
    userPassword = input("Enter your account password: ")
    print(accountList)

    for accountNumber, accountDetails in accountList.items():
        if accountNumber == userAccountNumber:
            if userPassword == accountList[accountNumber][2]:
                bankOperation()

    print("invalid user credential")
    userLogin()


def userRegistration():
    print("Welcome\nEnter your detail to register")
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    email = input("Enter your email address: ")
    Password = input("Enter your password: ")

    name = firstName + " " + lastName
    accountNumber = generateAccountNumber()
    accountDetails.append(name)
    accountDetails.append(email)
    accountDetails.append(Password)
    accountList.update({accountNumber: accountDetails})
    print("Registration successful")
    print(
        f"Your Account details is :\nyour account name is {name}\n________________________\nyour account email is :{email}\n________________________\nyour account "
        f"password is: {Password} \n________________________\nyour account number is {accountNumber}")
    print("keep your your detail save")
    userLogin()


def bankOperation():
    print("Select the an option")
    print("press 1 for Withdrawal \npress 2 for cash Deposit \npress 3 for Transfer\n press 4 to login\n press ")

    optionSelected = int(input("please select an option"))
    if optionSelected == 1:
        print("selected option is %s ", optionSelected)
        withdrawal()
    if optionSelected == 2:
        print("selected option is %s ", optionSelected)
        deposit()
    if optionSelected == 3:
        print("selected option is %s ", optionSelected)
        transfer()
    if optionSelected == 4:
        print("selected option is %s ", optionSelected)
        logout()


def generateAccountNumber():
    return random.randrange(1111111111, 9999999999)


def withdrawal():
    global total_balance
    withdrawAmount = int(input("Enter the withdraw amount"))
    if withdrawAmount < total_balance:
        if total_balance > 0:
            total_balance = total_balance - withdrawAmount
            print("Your new balance is : " + str(total_balance))
            bankOperation()
        else:
            print("insufficient fund")


def deposit(balance=0):
    global total_balance
    depositAmount = int(input('Enter the amount to deposit'))
    if depositAmount > 0:
        total_balance = balance + depositAmount
        print("Your new balance is : " + str(total_balance))
        bankOperation()
    else:
        print("invalid Amount")


def transfer(balance=0):
    global total_balance
    transfer_Acount = int(input("Enter account number"))
    amount = int(input('Enter the amount to transfer'))
    if amount > balance:
        total_balance = balance + amount
        print(f"your transfer to {transfer_Acount} is successful")
        print("Your new balance is : " + str(total_balance))
        bankOperation()
    else:
        print("invalid Amount")


def logout():
    userLogin()

    Begin()


if __name__ == '__main__':
    Begin()
