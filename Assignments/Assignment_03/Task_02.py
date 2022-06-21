# Write your code here
class Course:
    def __init__(self,course,instructor,sec):
        self.course = course
        self.instructor = instructor
        self.sec = sec

    def detail(self):
        print(f"{self.course} - {self.instructor} - {self.sec}")




#=========================================
c1 = Course("CSE110", "TBA", 8)
c1.detail()
print("===============")
c2 = Course("CSE111", "TBA", 9)
c2.detail()