import turtle               # allows us to use the turtles library

wn = turtle.Screen()        # creates a graphics window

alex = turtle.Turtle()      # create a turtle named alex

normalDistance = 50

class DrawObject:
    def __init__(self,turtle):
        self._alex = turtle

    def draw(self):
        print("Draw is not implemented")
        
        

class Square(DrawObject):
    def __init__(self,turtle,length=normalDistance):
        super(Square, self).__init__(turtle)
        self.length = length
        self.draw()
        
    def draw(self):
        for i in range(4):
            self._alex.forward(self.length)
            self._alex.right(360 / 4)

class Triangle(DrawObject):
    def __init__(self,turtle,length=normalDistance):
        super(Triangle, self).__init__(turtle)
        self.lenth = length
        self.draw()
        
        
    def draw(self):
        for i in range(3):
            self._alex.forward(self.lenth)
            self._alex.left(360/3)

class Line(DrawObject):
    def __init__(self,turtle,length=normalDistance,angle=0):
        super(Line, self).__init__(turtle)
        self.length = length
        self.angle = angle
        self.draw()
        
    def draw(self):
        self._alex.right(self.angle)
        self._alex.forward(self.length)
            
class Circle(DrawObject):
    def __init__(self,turtle,length=normalDistance):
        super(Circle, self).__init__(turtle)
        self.length = length
        self.draw()
        
    def draw(self):
        self.length/=360//10
        for i in range(360//10):
            self._alex.left(10)
            self._alex.forward(self.length)

# usage

for i in range(100):
    alex.speed(1000)
    Square(alex,normalDistance + i)
    Triangle(alex,normalDistance + i)
    Line(alex, normalDistance + i, 50)

    Square(alex,normalDistance + i)
    Triangle(alex,normalDistance + i)
    Line(alex, normalDistance + i, 50)

    Square(alex,normalDistance + i)
    Triangle(alex,normalDistance + i)
    Line(alex, normalDistance + i, 50)
    Circle(alex,normalDistance + i)

turtle.mainloop()