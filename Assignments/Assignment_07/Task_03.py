class Tournament:
    def __init__(self,name='Default'):
        self.__name = name
    def set_name(self,name):
        self.__name = name
    def get_name(self):
        return self.__name

class Cricket_Tournament(Tournament):
    def __init__(self,name='Default',team=0,type="No Type"):
        self.__name = name
        self.__team = team
        self.__type = type

    def detail(self):
        return f"Cricket Tournament Name: {self.__name}\nNumber of Teams: {self.__team}\nType: {self.__type}"

class Tennis_Tournament(Tournament):
    def __init__(self,name,players):
        self.__name = name
        self.__players = players

    def detail(self):
        return f"Tennis Tournament Name: {self.__name}\nNumber of Players: {self.__players}"


#write your code here

ct1 = Cricket_Tournament()
print(ct1.detail())
print("-----------------------")
ct2 = Cricket_Tournament("IPL",10,"t20")
print(ct2.detail())
print("-----------------------")
tt = Tennis_Tournament("Roland Garros",128)
print(tt.detail())
