import turtle

class Polygon:
    def __init__(self, sides, name, size=100, color="blue", line_thickness=4):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.line_thickness = line_thickness
        self.interior_angles = (self.sides - 2)*180
        self.angle = self.interior_angles/self.sides

    def draw(self):
        turtle.begin_fill()
        turtle.color(self.color)
        turtle.pensize(self.line_thickness)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
        turtle.end_fill()

class Square(Polygon):
    def __init__(self):
        super().__init__(4, "square")

    def draw(self):
        super().draw()

# square = Square()
# square.draw()
# turtle.done()

hexagon = Polygon(6, "hexagon", color="pink")
hexagon.draw()
turtle.done()