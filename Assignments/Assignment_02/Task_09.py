class buttons():
    def __init__(self,word,space,border):
        self.word = word
        self.space = space
        self.border = border
        self.brdrchrctr =  1 + self.space + len(word) + self.space + 1
        print(f"{self.word} Button Specification")
        print("Button name:",self.word)
        print('Number of the border characters for the top and the bottom:',self.brdrchrctr)
        print(self.border*self.brdrchrctr)
        print(self.border, ' '*self.space,self.word,' '*self.space,self.border,sep="")
        print(self.border * self.brdrchrctr)

#Write your class code here

word = "CANCEL"
spaces = 10
border = 'x'
b1 = buttons(word, spaces, border)
print("=======================================================")
b2 = buttons("Notify",3, '!')
print("=======================================================")
b3 = buttons('SAVE PROGRESS', 5, '$')
