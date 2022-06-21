class Calculator:
    
    def __init__(self,oper,val1,val2):
        self.operator = oper
        self.value1 = val1
        self.value2 = val2
        print("Let's calculate")

    def add(self):
        return(f"Result: {self.value1+self.value2}")

    def subtract(self):
        return(print(f"Result: {self.value1-self.value2}"))

    def multiply(self):
        return (f"Result: {self.value1 * self.value2}")

    def divide(self):
        return(f"Result: {self.value1 / self.value2}")

    def calculate(self):
        if self.operator == "+":
            print(self.add())
        elif self.operator == "-":
            print(self.subtract())
        elif self.operator == "*":
            print(self.multiply())
        elif self.operator == "/":
            print(self.divide())


operator = input("What operation do you want? ")
value1 = int(input("Enter 1st value: "))
value2 = int(input("Enter 2nd value: "))
math = Calculator(operator,value1,value2)
math.calculate()
