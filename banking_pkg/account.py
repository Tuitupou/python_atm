def show_balance(balance):
    print("Your current balance is: $" + str(balance))

def deposit(balance):
    amount = input("Enter amount to deposit: $")
    return balance + int(amount)

def withdraw(balance):
    while True:
        amount = input("Enter amount to withdraw: $")
        if int(amount) > balance:
            print("Sorry. You do not have appropriate funds")
            print("Here is your current balance: $" + str(balance))
        else:
            break
    
    return balance - int(amount)

def logout(name):
    print("Goodbye", name + "!")