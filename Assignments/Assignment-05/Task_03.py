class Team:
    def __init__(self,t="New team"):
        self.__name = t
        self.__players = []

    def setName(self,n):
        self.__name = n

    def addPlayer(self,obj):
        self.__players.append(obj)

    def printDetail(self):
        print('=====================')
        print(f"Team: {self.__name}")
        print("List of Players:")
        print(self.__players)
        print('=====================')

class Player:
    def __init__(self,n):
        self.name = n
    def __repr__(self):
        return self.name

# Write your code here for subtasks 1-4

b = Team()
b.setName('Bangladesh')
mashrafi = Player("Mashrafi")
b.addPlayer(mashrafi)
tamim = Player("Tamim")
b.addPlayer(tamim)
b.printDetail()
a = Team("Australia")
ponting = Player("Ponting")
a.addPlayer(ponting)
lee = Player("Lee")
a.addPlayer(lee)
a.printDetail()
