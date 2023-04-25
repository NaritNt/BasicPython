import turtle

tao = turtle.Pen()

def circle():
    for i in range(20):
       tao.forward(150)
       tao.left(150)
def rotate(x, y):
    tao.penup()
    tao.goto(x, y)
    tao.pendown()
circle()
rotate(-100, 100)
circle()
