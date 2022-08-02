# Write your code here
class Color:
    def __init__(self,n):
        self.clr = n

    def __add__(self, other):
        temp = [self.clr,other.clr]
        if "red" in temp and 'yellow' in temp:
            return Color("Orange")
        elif "blue" in temp and "yellow" in temp:
            return Color("Green")
        elif "red" in temp and "blue" in temp:
            return Color("Violet")

# Do not change the following lines of code

C1 = Color(input("First Color: ").lower())
C2 = Color(input("Second Color: ").lower())
C3 = C1 + C2
print("Color formed:", C3.clr)
