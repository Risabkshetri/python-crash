# Create a class Rectangle with length and breadth with following constructor and methods:
# a) default constructor
# b) Parameterized constructor
# c) area() to compute area of rectangle

class Rectangle:
    def __init__ (self, l=10, b=20):
        self.length = l
        self.breadth = b
        print("Area = ", self.length * self.breadth)
    
    def area(self,length, breadth):
        return length * breadth

r1 = Rectangle()
r2 = Rectangle(20, 30)
print("Area of r1 = ", r1.area(70, 20))



