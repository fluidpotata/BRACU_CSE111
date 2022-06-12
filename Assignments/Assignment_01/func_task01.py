''''''
'''
You are one of the gym instructors at AmiKenoMota. You decide to provide a
customized diet and exercise plans based on the BMI of an individual. You
measure the weight in kilograms and height in meters and calculate the BMI
before a plan can be decided. Write a BMI function that takes in two values,
weight in kg and height in cm and print the score along with the condition. (Make
sure to convert cm into m before calculation)
BMI(height, weight)

                    BMI = kg/m2
Based on the BMI score return the following output.

            ● < 18.5- Underweight
            ● 18.5 - 24.9 - Normal
            ● 25 -30 - Overweight
            ● > 30 – Obese
            
Sample Input                Sample Output
(175, 96)                   Score is 31.3. You are Obese
(152, 48)                   Score is 20.8. You are Normal
'''

def BMI(height,weight):
    height = height/100
    bmi = weight/(height**2)
    bmi = bmi.__round__(1)
    print("Score is",bmi,", You are",end=" ")
    if bmi<18.5:
        print("Underweight")
    elif 18.5<=bmi<=24.9:
        print("Normal")
    elif 25<=bmi<=30:
        print("Overweight")
    elif bmi>30:
        print("Obese")

BMI(152,48)