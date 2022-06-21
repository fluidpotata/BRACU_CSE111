
class Shinobi:
    def __init__(self,param1,param2):
        self.name = param1
        self.rank = param2
        self.missionnum = 0
        self.salary = 0

    def calSalary(self,missionnum):
        self.missionnum = missionnum
        if self.rank == 'Genin':
            self.salary = missionnum * 50
        elif self.rank == 'Chunin':
            self.salary = missionnum *100
        else:
            self.salary = missionnum*500

    def printInfo(self):
        print("Name:",self.name)
        print("Rank:",self.rank)
        print("Number of mission:",self.missionnum)
        print("Salary:",self.salary)

    def changeRank(self,rank):
        self.rank = rank


naruto = Shinobi("Naruto", "Genin")
naruto.calSalary(5)
naruto.printInfo()
print('====================')
shikamaru = Shinobi('Shikamaru', "Genin")
shikamaru.printInfo()
shikamaru.changeRank("Chunin")
shikamaru.calSalary(10)
shikamaru.printInfo()
print('====================')
neiji = Shinobi("Neiji", "Jonin")
neiji.calSalary(5)
neiji.printInfo()
