# Write your code here.
class Match:
    def __init__(self,teams):
        self.bat = teams.split('-')[0]
        self.bowl = teams.split('-')[1]
        print('5..4..3..2..1.. Play !!!')
        self.over = 0
        self.wicket = 0
        self.run = 1

    def add_run(self,run):
        self.run += run

    def add_over(self,ovr):
        self.over += ovr
        if self.over>=5:
            print(f"Warning! Cannot add {ovr} over/s (5 over match)")
            self.over -= ovr

    def add_wicket(self,wckt):
        self.wicket += 1

    def print_scoreboard(self):
        return f"Batting Team: {self.bat} \nBowling Team: {self.bowl} \nTotal Runs: {self.run} Wickets: {self.wicket} Overs: {self.over}"
#=================================================
match1 = Match("Rangpur Riders-Cumilla Victorians")
print("=========================")
match1.add_run(4)
match1.add_run(6)
match1.add_over(1)
print(match1.print_scoreboard())
print("=========================")
match1.add_over(5)
print("=========================")
match1.add_wicket(1)
print(match1.print_scoreboard())
