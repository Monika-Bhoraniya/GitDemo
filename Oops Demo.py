#class are user defined prototype
#sum , multiplication, addition,constant
#methods, class, variable,instance variable, constructor etc.

# self keyword is mandatory for calling variable name into method
#instance
#constructor _init_

class Calculator:
    num = 100

    #default constructor
    def __init__(self,a,b):
        self.firstNumber = a
        self.SecondNumber = b
        print("i am called constructor")

    def getData(self):
        print("Hello oops example")

     def Summation(self):
         return self.firstNumber + self.SecondNumber + Calculator.num


obj = Calculator(2,3) #syntax to cretae object in python
obj.getData()
print(obj.Summation)

obj = Calculator(4,5)
obj.getData()
print(obj.num)
