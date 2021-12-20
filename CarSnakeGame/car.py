import turtle as t
import random as rd

t.bgcolor('grey')

car = t.Turtle()
car.shape('square')
car.speed(0)
car.penup()
car.hideturtle()

pylon = t.Turtle()
pylon_shape = ((0,0),(14,2),(18,6),(20,20),(6,18),(2,14))
t.register_shape('pylon',pylon_shape)
pylon.shape('pylon')
pylon.color('orange')
pylon.penup()
pylon.hideturtle()
pylon.speed()

game_started = False
text_pylon = t.Turtle()
text_pylon.write('Please press your SPACE bar to start!', align='center', font=('Arial',18,'bold'))
text_pylon.hideturtle()

score_pylon = t.Turtle()
score_pylon.hideturtle()
score_pylon.speed(0)


def outside_window():
    left_wall = -t.window_width()/2 
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2 
    bottom_wall = -t.window_height()/2
    (x,y) = car.pos()
    outside = x < left_wall or  x > right_wall or  y < bottom_wall or y > top_wall
    return outside


def game_over():
    car.color('grey')
    pylon.color('grey')
    t.penup()
    t.hideturtle()
    t.write('GAME OVER', align='center', font=('Arial', 30,'normal'))



def display_score(current_score):
    score_pylon.clear()
    score_pylon.penup()
    x = (t.window_width() /2)-50
    y = (t.window_height() /2)-50
    score_pylon.setpos(x,y)
    score_pylon.write(str(current_score), align ='right', font=('Arial',40,'bold'))


def place_pylon():
    pylon.hideturtle()
    pylon.setx(rd.randint(-200,200))
    pylon.sety(rd.randint(-200,200))
    pylon.showturtle()


    
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0 
    text_pylon.clear()

    car_speed = 2
    car_length = 3
    car.shapesize(1,car_length,1)
    car.showturtle()
    display_score(score)
    place_pylon()

    while True:
        car.forward(car_speed)
        if car.distance(pylon)<20:
            place_pylon()
            car_length = car_length + 1
            car.shapesize(1,car_length,1)
            car_speed = car_speed + 1
            score = score + 10
            display_score(10)
            display_score(score)
        if outside_window():
            game_over()
            break


def move_up():
    if car.heading() == 0 or car.heading() == 180:
        car.setheading(90)

def move_down():
    if car.heading() == 0 or car.heading() == 180:
        car.setheading(270)

def move_left():
     if car.heading() == 90 or car.heading() == 270:
        car.setheading(180)


def move_right():
    if car.heading() == 90 or car.heading() == 270:
        car.setheading(0)


t.onkey(start_game, 'space')
t.onkey(move_up,'Up')
t.onkey(move_down,'Down')
t.onkey(move_left,'Left')
t.onkey(move_right,'Right')

t.listen()
t.mainloop()








