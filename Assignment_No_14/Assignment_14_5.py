class BankAccount:
    def __init__(self,account_number,name,balance):
        self.Account_No = account_number
        self.Name = name
        self.Balance = balance
    
    def Deposit(self):
        add_amount = int(input("Enter Amount To Deposit :- "))
        deposit_amount = self.Balance + add_amount
        print("Deposite Amount :-",deposit_amount)

    def Withdraw(self):
        remove_amount = int(input("Enter Amount to Withdraw :-"))
        withdraw_amount = self.Balance - remove_amount
        print("WithDraw Amount is :-",withdraw_amount)

    def Display(self):
        print("Account Number is :-",self.Account_No)
        print("Name is :-",self.Name)
        print("Account Balance is :- ",self.Balance)


def main():

    obj = BankAccount(10101010,"Mansi",50000)

    obj.Display()
    print("------------------------------")
    obj.Deposit()
    print("-----------------------------------")
    obj.Withdraw()

if __name__ =="__main__":
    main()