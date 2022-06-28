class Quiz:
    def __init__(self,course,mark,total=20):
        self.course = course
        self.mark = mark
        self.total = total

    def printDetails(self):
        print(f"Course: {self.course}")
        print(f"Marks: {self.mark}")
        print(f"Total Mark: {self.total}")

#+========================
Quiz1 = Quiz('CSE110',15)
Quiz1.printDetails()
print('-----------------')
Quiz2 = Quiz('CSE111',20,30)
Quiz2.printDetails()