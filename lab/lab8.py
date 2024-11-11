# # Create a class Rectangle with length and breadth with following constructor and methods:
# # a) default constructor
# # b) Parameterized constructor
# # c) area() to compute area of rectangle

# class Rectangle:
#     def __init__ (self, l=10, b=20):
#         self.length = l
#         self.breadth = b
#         print("Area = ", self.length * self.breadth)
    
#     def area(self,length, breadth):
#         return length * breadth

# r1 = Rectangle()
# r2 = Rectangle(20, 30)
# print("Area of r1 = ", r1.area(70, 20))



#Python program to create calculator class Include methods for basic arethmetic operations
class Calculator:
    def __init__ (self, x, y):
        self.a = x
        self.b = y
    
    def add(self):
        return self.a + self.b
    
    def sub(self):
        return self.a - self.b
    
    def mul(self):
        return self.a * self.b
    
    def div(self):
        return self.a / self.b
    

c1 = Calculator(10, 20)
print("Addition = ", c1.add())
print("Subtraction = ", c1.sub())
print("Multiplication = ", c1.mul())
print("Division = ", c1.div())
