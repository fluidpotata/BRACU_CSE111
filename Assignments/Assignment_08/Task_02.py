class RealNumber:
    def __init__(self, number=0):
        self.number = number

    def __add__(self, anotherRealNumber):
        return self.number + anotherRealNumber.number

    def __sub__(self, anotherRealNumber):
        return self.number - anotherRealNumber.number

    def __str__(self):
        return str(self.number)

#===========================================
class ComplexNumber(RealNumber):
    def __init__(self,r=0,i=0):
        if type(r)==int:
            super().__init__(r)
        else:
            super().__init__(r.number)
        self.imaginary = i

    def __add__(self, other):
        number = self.number + other.number
        imaginary = self.imaginary + other.imaginary
        return ComplexNumber(number,imaginary)




    def __sub__(self,other):
        number = self.number - other.number
        imaginary = self.imaginary - other.imaginary
        return ComplexNumber(number, imaginary)


    def __str__(self):
        x = str(self.number)
        if self.imaginary>0:
            x+=f" + {self.imaginary}i"
        else:
            x+=f" - {-1*self.imaginary}i"
        return x

#===========================================
r1 = RealNumber(3)
r2 = RealNumber(5)
print(r1 + r2)
cn1 = ComplexNumber(2, 1)
print(cn1)
cn2 = ComplexNumber(r1, 5)
print(cn2)
cn3 = cn1 + cn2
print(cn3)
cn4 = cn1 - cn2
print(cn4)
