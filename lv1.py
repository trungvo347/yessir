import character
import turtle


turtle.listen()
turtle.onkey(character.move_left, 'Left')
turtle.onkey(character.move_right, 'Right')
turtle.onkey(character.move_up, 'Up')
turtle.onkey(character.move_down, 'Down')