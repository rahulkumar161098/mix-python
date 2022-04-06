import sys

# Bank System 

class Customer:
    bankName= 'YesBank'
    def __init__(self, name, balance=0):
        self.name= name
        self.balance= balance

    def show(self):
        print('your name is :', self.name)
        print('your balane is :', self.balance)
        
    def deposit(self, amt):
        self.balance=self.balance+amt
        print('Your current balance is: ', self.balance)
    
    def credit(self, crd):
        if crd>self.balance:
            print("you have insefficient fund\n")
        else:
            self.balance= self.balance-crd
            print("your remaining balance is : ", self.balance)

print('Welcome to ', Customer.bankName)
name= input("Enter your name : ")
c=Customer(name)
while True:
    print('b- for balance\nd - for deposit : \nw - for withdraw : \ne - for exit : ')
    option= input('Choose your option :\n ')
    
    if option == 'd' or option == 'D':
        amt= float(input("Enter your amount to deposit : \n"))
        c.deposit(amt)
    elif option == 'w' or option == 'W':
        crd= float(input('Enter your amount to withdraw : \n'))
        c.credit(crd)
    elif option == 'b' or option== 'B':
        c.show()
    elif option== 'e' or option== 'E':
        print('Thanks for Banking')
        sys.exit()
    else:
        print("Please choose valid option")