data = {
    1234: {'balance':8000, 'transactions':[]},
    2341: {'balance':16000, 'transactions':[]},
    3412: {'balance':90000, 'transactions':[]},
    4123: {'balance':50000, 'transactions':[]},
}

def login(pin):
    if pin in data:
        print("Login Successful")
        return True
    else:
        print("Invalid pin. Try Again!!!")
        return False
    
def checkbalance(pin):
    print(f"Balance Amount: ₹{data[pin]['balance']}")    

def deposit(pin):
    amount = int(input("Enter the amount: "))
    data[pin]['balance']+=amount
    data[pin]['transactions'].append(f'₹{amount} is deposited+++++')
    print("Deposit Successful")

def withdraw(pin):
    amount = int(input("Enter the withdraw amount: "))
    if amount <= data[pin]['balance']:
        data[pin]['balance']-=amount
        data[pin]['transactions'].append(f'₹{amount} is withdraw-----')
        print("Amount is Withdraw Successful")
    else:
        print("Insufficinet Balance")

def view_Transactions(pin):
    if data[pin]['transactions']:
        print("Transaction Histroy: ")
        for i in data[pin]['transactions']:
            print(i)
        else:
            print("End of Transactions")
    else:
        print("No Transactions")            


u_pin = int(input("Enter the pin: ")) 
if login(u_pin):

    while True:
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. View Transactions")
        print("0. Exit")   

        ch = int(input("Enter the choice: "))
        if ch==1:
            checkbalance(u_pin)
        elif ch==2:
            deposit(u_pin)
        elif ch==3:
            withdraw(u_pin) 
        elif ch==4:
            view_Transactions(u_pin)
        elif ch==0:
            print("Thankyou")
            break
        else:
            print("Invalid choice")    


# Types of Functions
# 1. Built-in Functions
# Examples:
print(len("Hello")) # Output: 5
print(abs(-10)) # Output: 10
print(max(1, 5, 3)) # Output: 5
print(sorted([3, 1, 4, 2])) # Output: [1, 2, 3, 4]

# 2. User-Defined Functions
# Examples:
def add(a,b):
    return a+b
print(add(5,10))
