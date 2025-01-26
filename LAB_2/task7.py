# overloading Calculator
class Calculator:
    def add(self, a,b,c=0):
        return a+b+c
    
calc=Calculator()
print("Addition of Two Numbers: ",calc.add(10,20))
print("Addition of Thrree Numbers: ",calc.add(10,2,30))

