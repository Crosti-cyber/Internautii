import turtle
s = turtle.Screen()
s.setup(width=1000,height=1000)
turtle.title("Lipsa de Comunicare")
tr = turtle.Turtle()
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
        tr.circle(360,54)
    elif (dir == 2):
        tr.rt(45)
        tr.circle(-360,54)
    else: print("err")
def FacialFeatures(sx,sy,dir):
    def trstart(offx,offy):
        tr.pu()
        tr.goto(sx+offx,sy+offy)
        tr.pd()
        tr.setheading(tr.towards(0,0))
    if (dir == 1):
        trstart(0,0)
        tr.dot(15)
        trstart(20,-90)
        tr.rt(180)
        tr.circle(-100,35)
    elif (dir == 2):
        trstart(0,0)
        tr.dot(15)
        trstart(20,-90)
        tr.circle(-100,35)
def Coarda1(r):
    tr.circle(r,-104)
    tr.right(180)
    tr.right(90)
    tr.speed(7)
def Coarda2(r):
    tr.pu()
    tr.goto(165,-85)
    tr.pd()
    tr.circle(r,-75)
    tr.right(180)
    tr.right(90)
    tr.speed(7)
FacialFeatures(-220,125,1)
FacialFeatures(220,125,2)
RombContur(0,-250)
RombOameni(160,-90,2)
RombOameni(-160,-90,1)
Coarda1(-285)
Coarda2(-263)
s.exitonclick()