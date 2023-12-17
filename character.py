import turtle

screnn = turtle.Screen
player= turtle.Turtle()
player.speed(0)
player.penup()
playerSpeed = 5

def move_left() :
    x = player.xcor() - playerSpeed
    player.setx(x)
    
def move_right() :
    x = player.xcor() - playerSpeed
    player.setx(x)
    
def move_up() :
    y = player.ycor() - playerSpeed
    player.sety(y)
    
def move_down() :
    y = player.ycor() - playerSpeed
    player.set(y)
