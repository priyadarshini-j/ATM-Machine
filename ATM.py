from datetime import datetime
now = datetime.now()

pin = 1234
balance = 1000
t_history = []
user_pin = int(input("Enter pin: "))

def display_option():
    print("1.Transaction History")
    print("2.Withdraw")
    print("3.Deposit")
    print("4.Transfer")
    print("5.Balance")
    print("6.Quit")
    user_input = int(input("Select option: "))
    return user_input

def withdraw():
    global balance
    withdraw_amt = int(input("Enter the withdraw amount: "))
    balance=balance-withdraw_amt
    t_history.append({"date":now.strftime("%d/%m/%Y %H:%M:%S"),"type":"withdraw","recipient_account_number":"","amount":withdraw_amt})
    print("Amount Withdraw Successfully")

def deposit():
    global balance
    deposit_amt = int(input("Enter the deposit amount: "))
    balance = balance + deposit_amt
    t_history.append({"date":now.strftime("%d/%m/%Y %H:%M:%S"),"type":"deposit","recipient_account_number":"","amount":deposit_amt})
    print("Amount Deposited Successfully")

def display_transaction():
    print("{:<5} {:<20} {:<10} {:<20} {:<10}".format('S.NO','DATE','TYPE','To','AMOUNT'))
    for ind, item in enumerate(t_history):
         print("{:<5} {:<20} {:<10} {:<20} {:<10}".format(ind+1,item["date"],item["type"],item["recipient_account_number"],item["amount"]))

def transfer():
    global balance
    account_no = int(input("Enter The Recipient Account Number: "))
    transfer_amt = int(input("Enter the amount: "))
    balance=balance-transfer_amt
    t_history.append({"date":now.strftime("%d/%m/%Y %H:%M:%S"),"type":"transfer","amount":transfer_amt,"recipient_account_number":account_no})
    print("Amount Transfer Successfully")

    
if user_pin == pin:
    user_select=display_option()
    temp_flag = False
    while user_select != 6:
        if temp_flag == True:
            user_continue = input("Do you want continue?(Yes/No): ")
            if user_continue == "Yes":
                user_select=display_option()
            else:
               user_select=6
               break;
            
        if user_select == 1:
            display_transaction()
            temp_flag= True
        elif user_select == 2:
            withdraw()
            temp_flag=True
        elif user_select == 3:
            deposit()
            temp_flag=True
        elif user_select == 4:
            transfer()
            temp_flag=True
        elif user_select == 5:
            print(f"Available Balance:{balance}")
            temp_flag=True
        elif user_select == 6:
            continue;
        else:
            print("Please Select Valid Option")
            temp_flag = True
