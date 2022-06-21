# Write your code here
class Calculator:
    def __init__(self):
        pass
    def calculate(self,num1,num2,op):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        if op == "+":
            self.result = num1+num2
            return self.result
        elif op == "-":
            self.result = num1-num2
            return self.result
        elif op == "*":
            self.result = num1*num2
            return self.result
        elif op == "/":
            self.result = num1/num2
            return self.result

    def showCalculation(self):
        print(f"{self.num1} {self.op} {self.num2} = {self.result}")
#==========================

c1 = Calculator()
print("==================")
val = c1.calculate(10, 20, '+')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 10, '-')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 5, '*')
print("Returned value:", val)
c1.showCalculation()
print("==================")
val = c1.calculate(val, 16, '/')
print("Returned value:", val)
c1.showCalculation()
