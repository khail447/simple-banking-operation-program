# register function- email, first name, last name, password
# login function- account number, password
# homepage function
# generate account number function
# bank operation function- withdrawal, deposit, 
# withdrawal function
# deposit function


import random
database= {}
# initialize function
def init():
    print("***WELCOME TO ZURI BANK***")
    newuser= int(input('''Do you have an account with us: 
    1. Yes
    2. No \n'''))
    if newuser == 1:
        login()
    elif newuser==2:
        print(register())
    else:
        print("you've selected an invalid option")
        init()

def login():
    print("***Login to your account***")
    login_accountnumb= int(input("Please input your account number: \n"))
    login_password= input("Please input your password: \n")
    for accountnumber,userdetails in database.items():
        if accountnumber==login_accountnumb:
            if userdetails[3]==login_password:
                homepage(userdetails)
        else:
            print("You have inputed the wrong account number or password. please try again")
            login()

def register():
    print("***CREATE AN ACCOUNT***")
    email= input("please input your email address \n")
    first_name= input("Please input your first name \n")
    last_name= input("please input your last name \n")
    password= input("please input your password \n")
    balance= 0
    accountnumber= accountnumbergenerated()
    database[accountnumber] = [first_name, last_name, email, password, balance]

    print("your account has been created")
    print(f'your account number is: {accountnumber}')
    login()

def homepage(user):
    print(f"***WELCOME {user[0]} {user[1]}***")
    print(f"account balance: {user[4]}")
    banktransaction= int(input('''Do u want to perform a transaction? 
    1. yes
    2. no \n'''))
    if banktransaction==1:
        bankoperation(user)
    elif banktransaction== 2:
        login()
    else:
        print('You have entered an incorrect option. Please try again')
        homepage(user)

def bankoperation(user):
    print("What would u like to do: \n")
    selectoperation= int(input("1. Withdrawal \n2. Deposit \n3. Transfer \n4. Back to home page \n5. Logout \n6. Exit \n"))
    if selectoperation== 1:
        withdrawal(user)
    elif selectoperation==2:
        deposit(user)
    elif selectoperation==3:
        transfer()
    elif selectoperation==4:
        homepage(user)
    elif selectoperation==5:
        login()
    elif selectoperation==6:
        exit()
    else:
        print('You have entered an incorrect option. Please try again')
        bankoperation()

def withdrawal(user):
    withdrawalamount= int(input("please input the amount you'd like to withdraw: \n"))
    balance= user[4]
    if withdrawalamount<balance:
        print("withdrawal successful")
    elif withdrawalamount>balance:
        print("Insufficient balance")
    else:
        print("you have entered an incorrect amount. try again")
        withdrawal(user)

def deposit(user):
    depositamount= int(input("How much would you like to deposit? \n"))
    balance= user[4]
    newbalance= depositamount+balance
    print(f"Your deposit has been approved. Your new account balance is {newbalance}")

def transfer():
    print("transfer")

def accountnumbergenerated():
    return random.randrange(1111111111,9999999999)



init()