import turtle
s = turtle.Screen()
s.setup(width=1000,height=1000)
turtle.title("Lipsa de Comunicare")
tr = turtle.Turtle()
tr.hideturtle()
def RombContur(sx,sy):
    def trstart(offx,offy):
        tr.pu()
        tr.goto(sx+offx,sy+offy)
        tr.pd()
        tr.setheading(tr.towards(0,0))
    tr.pu()
    tr.goto(sx,sy)
    tr.pd()
    tr.pencolor('black')
    tr.setheading(tr.towards(0,0))
    tr.pensize(3)
    tr.rt(45)
    tr.forward(500)
    tr.lt(90)
    tr.fd(500)
    trstart(0,0)
    tr.lt(45)
    tr.forward(500)
    tr.rt(90)
    tr.fd(500)
    trstart(0,0)
def RombOameni(sx,sy,dir):
    def trstart(offx,offy):
        tr.pu()
        tr.goto(sx+offx,sy+offy)
        tr.pd()
        tr.setheading(tr.towards(0,0))
    trstart(0,0)
    if (dir == 1):
        tr.lt(45)
        tr.circle(250,70)
    elif (dir == 2):
        tr.rt(45)
        tr.circle(-250,70)
    else: print("err")
RombContur(0,-250)
RombOameni(175,-50,2)
RombOameni(-175,-50,1)

a=0
input(a)