# Write your code here
class PlayerEarning:

    def __init__(self,name):
        self.name = name
        self.earning, self.bonus, self.total = 0, 0, 0

    def calculateTotal(self,main,goal=0):
        self.earning = main
        # self.bonus = bonus
        if goal>30:
            self.bonus = (5/100)*self.earning + 10000
        elif goal == 0:
            self.bonus = 0
        else:
            self.bonus = (5 / 100) * self.earning
        self.total = self.earning+self.bonus
    def printDetails(self):
        print(f"Player Name: {self.name}\nPlayer Season Earning without bonus: {self.earning}")
        print("Bonus:", self.bonus)
        print("Player Season Earning after Bonus:", self.total)





#====================================
print("**********************")
player1 = PlayerEarning('Buffon')
player1.calculateTotal(250000)
player1.printDetails()
print("\n**********************")
player2 = PlayerEarning('Dybala')
player2.calculateTotal(250000,31)
player2.printDetails()
print("\n**********************")
player3 =PlayerEarning('Cuadrado')
player3.calculateTotal(250000,20)
player3.printDetails()