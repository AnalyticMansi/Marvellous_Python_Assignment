class BankAccount:

    ROI = 10.5

    def __init__(self):
        self.Name = input("Enter Your Name :- ") 
        self.Amount = float(input("Enter The Amount :- "))
        print("---------------------------------------")
    
    def Display(self):
        print("Account Holder Name :- ",self.Name)
        print("Account Balance is :- ",self.Amount)
        print("---------------------------------------------")

    def Deposit(self):
        deposit_amount = float(input("Enter Amount To Deposite :- "))
        self.Amount = self.Amount + deposit_amount
        print("New Balance Of Account is :-",self.Amount)
        print("------------------------------------------------------")
    
    def Withdraw(self):
        withdraw_amount = int(input("Enter Amount to withdraw :- "))
        if withdraw_amount <= self.Amount:
            self.Amount = self.Amount - withdraw_amount
            print("New Balance After Withdraw Amount is  :-",self.Amount)
            print("---------------------------------------------------")
        else:
            print("Insufficient Balance ")
            print("-------------------------------------------------")
        

    def CalculateInterest(self):
        intrest = (self.Amount / BankAccount.ROI) * 100
        print("Intrest of Current Balance is :- ",intrest)
        
    


def main():

    obj = BankAccount()

    obj.Display()
    obj.Deposit()
    obj.Withdraw()
    obj.CalculateInterest()
    

if __name__ =="__main__":
    main()