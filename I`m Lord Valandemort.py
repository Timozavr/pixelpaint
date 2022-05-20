import turtle

window = turtle.Screen()
I = turtle.Turtle()
window.listen()
#I.hideturtle()
speed = 5

def moveUp():
    x, y = I.position()
    I.setpos(x,y+speed)
def moveDown():
    x, y = I.position()
    I.setpos(x,y-speed)
def moveLeft():
    x, y = I.position()
    I.setpos(x-speed,y)
def moveRight():
    x, y = I.position()
    I.setpos(x+speed,y)
def change():
    if I.isvisible():
        I.up()
        I.hideturtle()
    else:
        I.down()
        I.showturtle()
def speedUp():
    global speed
    speed+=10
def speedDown():
    global speed
    speed = max(0,speed-10)
def Green():
    I.color('Green')
def Blue():
    I.color('Blue')
def Red():
    I.color('Red')
def pens1():
    I.pensize(0)
def pens2():
    I.pensize(3)
def pens3():
    I.pensize(6)
def pens4():
    I.pensize(9)
def pens5():
    I.pensize(12)
def pens6():
    I.pensize(15)
def pens7():
    I.pensize(18)
def DELITE():
    I.reset()
def T():
    x, y = I.position()
    I.setpos(x-speed,y+speed)
def U():
    x, y = I.position()
    I.setpos(x+speed,y+speed)
def B():
    x, y = I.position()
    I.setpos(x-speed,y-speed)
def M():
    x, y = I.position()
    I.setpos(x+speed,y-speed)

window.onkey(moveUp,"Up")
window.onkey(moveDown,"Down")
window.onkey(moveLeft,"Left")
window.onkey(moveRight,"Right")
window.onkey(change,"space")
window.onkey(speedUp,"w")
window.onkey(speedDown,"s")
window.onkey(Green,"1")
window.onkey(Blue,"2")
window.onkey(Red,"3")
window.onkey(pens1,"q")
window.onkey(pens2,"a")
window.onkey(pens3,"z")
window.onkey(pens4,"x")
window.onkey(pens5,"c")
window.onkey(pens6,"d")
window.onkey(pens7,"e")
window.onkey(DELITE,"g")
window.onkey(T,"t")
window.onkey(U,"u")
window.onkey(B,"b")
window.onkey(M,"m")

window.mainloop()
