class Batsman:
    def __init__(self,*args):
        if type(args[0]) == str:
            self.name = args[0]
            self.runsScored = args[1]
            self.ballsFaced = args[2]
        else:
            self.name = "New Name"
            self.runsScored = args[0]
            self.ballsFaced = args[1]
        self.strikerate = 0

    def printCareerStatistics(self):
        print(f"Name: {self.name} \nRuns Scored: {self.runsScored} , Balls Faced: {self.ballsFaced}")

    def battingStrikeRate(self):
        self.strikerate = (self.runsScored / self.ballsFaced)*100
        return self.strikerate

    def setName(self,strng):
        self.name = strng


b1 = Batsman(6101, 7380)
b1.printCareerStatistics()
print("============================")
b2 = Batsman("Liton Das", 678, 773)
b2.printCareerStatistics()
print("----------------------------")
print(b2.battingStrikeRate())
print("============================")
b1.setName("Shakib Al Hasan")
b1.printCareerStatistics()
print("----------------------------")
print(b1.battingStrikeRate())
