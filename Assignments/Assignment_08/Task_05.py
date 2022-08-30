class Exam:
    def __init__(self, marks):
        self.marks = marks
        self.time = 60

    def examSyllabus(self):
        return "Maths , English"

    def examParts(self):
        return "Part 1 - Maths\nPart 2 - English\n"
#=========================================================
class ScienceExam(Exam):
    def __init__(self,marks,time,*parts):
        super().__init__(marks)
        self.time = time
        self.parts = parts

    def examSyllabus(self):
        return super().examSyllabus()+" , "+" , ".join(self.parts)

    def examParts(self):
        x = super().examParts()
        for i in range(len(self.parts)):
            if i==len(self.parts)-1:
                x += f"Part {i + 3} - {self.parts[i]}"
            else:
                x += f"Part {i+3} - {self.parts[i]}\n"
        return x

    def __str__(self):
        return (f"Marks: {self.marks} Time: {self.time} minutes Number of Parts: {len(self.parts)}")


#=========================================================
engineering = ScienceExam(100, 90, "Physics", "HigherMaths")
print(engineering)
print('----------------------------------')
print(engineering.examSyllabus())
print(engineering.examParts())
print('==================================')
architecture = ScienceExam(100, 120, "Physics", "HigherMaths", "Drawing")
print(architecture)
print('----------------------------------')
print(architecture.examSyllabus())
print(architecture.examParts())