# Write your code here
class Account:
    count = 0
    def __init__(self,name,age,occ,am):
        self.name = name
        self.age = age
        self.occupation = occ
        self.amount = am
        Account.count += 1

    def addMoney(self,am):
        self.amount += am

    def withdrawMoney(self,am):
        self.amount -= am
        if self.amount<0:
            self.amount+=am

    def printDetails(self):
        print('Name:', self.name)
        print('Age:',self.age)
        print('Occupation:', self.occupation)
        print('Total Amount:', self.amount)

#================================================
print('No of account holders:', Account.count)
print("=========================")
p1 = Account("Abdul", 45, "Service Holder", 500000)
p1.addMoney(300000)
p1.printDetails()
print("=========================")
p2 = Account("Rahim", 55, "Businessman", 700000)
p2.withdrawMoney(700000)
p2.printDetails()
print("=========================")
p3 = Account("Ashraf", 62, "Govt. Officer", 200000)
p3.withdrawMoney(250000)
p3.printDetails()
print("=========================")
print('No of account holders:', Account.count)