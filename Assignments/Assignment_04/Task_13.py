# Write your code here
class Account:
    def __init__(self,n="Default Account",b=0):
        self.name = n
        self.balance = float(b)

    def details(self):
        return f"{self.name} \n{self.balance}"

    def withdraw(self,amount):
        self.balance -= amount
        if self.balance<=3070:
            print('Sorry, Withdraw unsuccessful! The account balance after deducting withdraw amount is equal to or less than minimum.')
            self.balance += amount
        else:
            print(f"Withdraw successful! New balance is: {self.balance}")



a1 = Account()
print(a1.details())
print("------------------------")
a1.name = "Oliver"
a1.balance = 10000.0
print(a1.details())
print("------------------------")
a2 = Account("Liam")
print(a2.details())
print("------------------------")
a3 = Account("Noah",400)
print(a3.details())
print("------------------------")
a1.withdraw(6930)
print("------------------------")
a2.withdraw(600)
print("------------------------")
a1.withdraw(6929)
