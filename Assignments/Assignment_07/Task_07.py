class Football:
  def __init__(self, team_name, name, role):
    self.__team = team_name
    self.__name = name
    self.role = role
    self.earning_per_match = 0

  def get_name_team(self):
    return 'Name: '+self.__name+', Team Name: ' +self.__team

#write your code here

class Player(Football):
  def __init__(self,team_name, name, role,goal,play):
    super().__init__(team_name, name, role)
    self.goal = goal
    self.played = play
    self.earning_per_match = (goal*1000) + (play*10)

  def calculate_ratio(self):
    self.ratio = self.goal/self.played


  def print_details(self):
    print(f"{super().get_name_team()}\nTeam role : {self.role} \nGoal Ratio: {self.ratio}\nMatch Earning: {self.earning_per_match}K")

class Manager(Football):
  def __init__(self, team_name, name, role, win):
    super().__init__(team_name, name, role)
    self.win = win
    self.salary = win*1000

  def print_details(self):
    print(f"{super().get_name_team()}\nTeam role : {self.role} \nTotal Win: {self.win}\nMatch earning: {self.salary}k")


player_one = Player('Juventus', 'Ronaldo', 'Striker', 25, 32)
player_one.calculate_ratio()
player_one.print_details()
print('------------------------------------------')
manager_one = Manager('Real Madrid', 'Zidane', 'Manager', 25)
manager_one.print_details()