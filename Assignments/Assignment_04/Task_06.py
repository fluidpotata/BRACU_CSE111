# Write your code here.
class Patient:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.symptom = []


    def add_Symptom(self,*n):
        for i in n:
            self.symptom.append(i)

    def printPatientDetail(self):
        print(f'Name: {self.name} \nAge: {self.age} \nSymptoms:',end=" ")
        for i in range(len(self.symptom)):
            if i==len(self.symptom)-1:
                print(self.symptom[i])
            else:
                print(self.symptom[i],end=", ")

#===============================
p1 = Patient('Thomas', 23)
p1.add_Symptom('Headache')
p2 = Patient('Carol', 20)
p2.add_Symptom('Vomiting', 'Coughing')
p3 = Patient('Mike', 25)
p3.add_Symptom('Fever', 'Headache', 'Coughing')
print("=========================")
p1.printPatientDetail()
print("=========================")
p2.printPatientDetail()
print("=========================")
p3.printPatientDetail()
