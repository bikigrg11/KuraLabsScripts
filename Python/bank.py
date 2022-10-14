import time
import datetime

class BankAccount(object):

    nums = 1000
    noOfUser = 0

    def __init__(self, username, balance):

        self.username = username
        self.balance = balance
        self.pinNumber = int(input(f"Hello {self.username}, Please enter 4 digit Pin Code for your new Account : "))
        self.accountNumber = BankAccount.nums
        BankAccount.nums = BankAccount.nums + 1
        BankAccount.noOfUser = BankAccount.noOfUser + 1
        self.transactions = []

        print(f"You have $ {balance} in your Account Number: {self.accountNumber} \n")
        print(f"Account Creation Complete ! We hope to see you again Soon {self.username} ! \n")
        print("=============================================================================")

    # this Method allows user to check his/her Pin to the account

    def check_pin(self):
        userPin = input(f"Hello {self.username}. Please enter your PIN Code:")
        # print(type(userPin))
        # print(type(self.pinNumber))

        if int(userPin) == self.pinNumber:
            print("Pin Code is correct !")
            return True
        else:
            print("Pin Code is not correct !")
            return False

    # this Method allows user to withdraw $ from his/her account

    def withdraw(self):
        print(f"Hello {self.username}. Your Current Balance is ${self.balance}")
        withdrawAmt = int(
            input("Please enter how much would you like to Withdraw: $"))
        if self.balance < withdrawAmt:
            print("Your Balance is less than Withdraw Amt")
        else:
            self.balance -= withdrawAmt
            print("Withdraw Complete")
            x = datetime.datetime.now()
            self.transactions.append(f"Withdrew ${withdrawAmt} - Account: {self.accountNumber} - Date: {x}")
            print(f"Your New Balance is ${self.balance}\n\n")

    # this Method allows user to deposit $ to his/her account

    def deposit(self):
        depositAmt = int(input(f"Hello {self.username}. Please enter how much would you like to Deposit: $"))
        if depositAmt <= 0:
            print("Deposit Balance cannot be less than or equals to 0")
        else:
            self.balance += depositAmt
            print("Deposit Complete")
            x = datetime.datetime.now()
            self.transactions.append(f"Deposit ${depositAmt} - Account: {self.accountNumber} - Date: {x}")
            print(f"Your New Balance is ${self.balance}")

    # this Method allows user to transfer $ from one account to another

    def transfer(self):
        if BankAccount.noOfUser < 2:
            print("Cannot Transfer $$$ with only 1 User, Please create new user first")
            return
        else:
            print("List of users you can transfer $$$ to:")
            for user,value in bankAccountList.items():
                print(user)
           
            toUser = input(f"Hello {self.username}, Choose a user who would like to TRANSFER To. :").lower()
            if toUser in bankAccountList.keys():
                transferAmount = int(input("Hello, How much would you like to TRANSFER. $"))
                if transferAmount < self.balance:
                    self.balance -= transferAmount
                    bankAccountList[toUser].balance += transferAmount
                    print("Transfering .....")
                    time.sleep(2)
                    print("Transfering .....")
                    time.sleep(2)

                    x = datetime.datetime.now()
                    self.transactions.append(f"Transfer Out ${transferAmount} from Account: {self.accountNumber} to : {toUser} - Date: {x}")
                    bankAccountList[toUser].transactions.append(f"Transfer In ${transferAmount} to Account: {bankAccountList[toUser].accountNumber} from : {self.username} - Date: {x}")

                    print("Transfer Complete")
                    print(f"Your New Balance is ${self.balance}")
                else:
                    print("Transfer Amount Cannot be Greater than your Current Balance")
            else:
                print(f"Cannot Find Account for {toUser}, Please Select a valid Account !")
    
    # this method is used to check all the past transactions recorded.
    def check_history(self):
        print("Past Transactions for User: {self.username}")
        print("---------------------------------------------")
        for transaction in self.transactions:
            print(transaction)

# ------------- class ends here --------------------- #

# This function will create new Account for the Bank

def newAccount():
    print(f"Welcome New User No:{BankAccount.noOfUser+1} ! to your Financial World !")
    print("You are walking to the BANK of KURALABS to open a new Bank Account.")
    print("Walk .... Walk ... Walk ...... \n ")
    time.sleep(5)

    print("You are Greeted by a Bank Representative.")
    time.sleep(3)
    name = input(
        "Hello ! Welcome to BANK of KURALABS. Whom do i have pleasure speaking with today? Name :").lower()
    print(f"Thank you ! {name} for choosing to Bank with KURALABS\n\n")
    initialDeposit = int(
        input(f"Hello {name}, How much would like to deposit today? $"))
    return BankAccount(name, initialDeposit)

# ------------- ATM BANK ------------------------- #

# This Function add ATM functionality to the Bank

def useATM(username, Account1):
    time.sleep(1)
    print(f"{username} is now walking to use an ATM Machine.")
    time.sleep(1)
    print(f"{username} reaches an ATM Machine. and Enters the Debit Card to the ATM. ")
    time.sleep(1)
    # Assume Debit card is Account 1

    wrongPin = 0
    userInput = None
    checkPin = False

    while userInput != "exit":

        # After user inserts the debit card check the PIN !
        if checkPin == False:
            checkPin = Account1.check_pin()

        if checkPin == True:
            # Security cleared User can now use the ATM. !
            print(
                "=============================================================================")
            options = input("What would you like to do Select : a, b, c, d or e\n \
                \n a) Check Balance \n b) Withdraw Money \n c) Deposit Money \n d) Transfer Money \n e) Check Past transactions \n f) EXIT \n Select:").lower()
            print("\n")
            if options == "a":  # check Balance
                print(f"Hello {Account1.username}, Your Current Balance is ${Account1.balance}")
            elif options == "b":  # Withdraw Money
                Account1.withdraw()
            elif options == "c":  # Deposit Money
                Account1.deposit()
            elif options == "d":  # Transfer Money
                Account1.transfer()
            elif options == "e": # check past Transactions
                Account1.check_history()
            elif options == "f":  # Exit ATM
                print("Thank you for using BANK of KURALABS !")
                print("=============================================================================")
                break
            else:
                print("Wrong Options")
                wrongPin += 1
        else:
            wrongPin += 1

        if wrongPin == 3:
            print("Too Many Wrong Attempts ")
            break

        time.sleep(2)

# --------------- Use Creation ------------------- #


def createUsers(num):
    for i in range(num):
        account = newAccount()
        bankAccountList[account.username] = account


# ------------------------------------ Main ------------------------------------------- #

bankAccountList = dict()


while True:
    print("=============================================================================")
    choice = input(
        "Welcome to the BANK OF KURALABS: \n a) New User Account Creation \n b) Use ATM Machine \n c) Exit \n Choice > ").lower()
    print("=============================================================================")
    if choice == "a":
        userNum = int(
            input("Hello, How many Users would you like to create today? "))
        createUsers(userNum)

    elif choice == "b":
        if BankAccount.noOfUser > 0:
            print("Available Users: ")
            for user, value in bankAccountList.items():
                print(user)
            
            chooseUser = input("Hello, Choose a user who would like to go to ATM Today. ").lower()

            if chooseUser in bankAccountList.keys():
                useATM(chooseUser, bankAccountList[chooseUser])
        else:
            print("No of Users is 0. Please create new Users first. ")

    elif choice == "c":
        print("Thank you for using this Simulation ! Have a good day Now !")
        break

    else:
        print("Wrong Input Please Enter again.")
