

import turtle



# 1. WASD를 이용해서 상하좌우 이동
# 2. 한번 이동 거리는 50
# 3. Esc 키 누르면 처음부터 다시 시작함

def WkeyMove():
    turtle.left(0)
    turtle.forward(50)
    turtle.stamp()

def AkeyMove():
    turtle.left(90)
    turtle.forward(50)
    turtle.stamp()

def SkeyMove():
    turtle.left(180)
    turtle.forward(50)
    turtle.stamp()

def DkeyMove():
    turtle.left(270)
    turtle.forward(50)
    turtle.stamp()

def restart():
    turtle.reset()

def gameLoop():
    turtle.reset()
    turtle.shape('turtle')
    turtle.listen() 
    while(True):
        turtle.onkey(restart,'Escape')
        turtle.onkey(WkeyMove,'w')
        turtle.onkey(AkeyMove,'a')
        turtle.onkey(SkeyMove,'s')
        turtle.onkey(DkeyMove,'d')

 



# 키 입력 기다림 

gameLoop()

turtle.exitonclick()


