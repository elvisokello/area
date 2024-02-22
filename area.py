class Circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*self.radius**2
    def perimeter(self):
        return 3.14*(self.radius+self.radius)
my_circle=Circle(8)
print("Radius:",my_circle.radius)
print("Circle:",my_circle.area())
print("Perimeter:",my_circle.perimeter())
    
