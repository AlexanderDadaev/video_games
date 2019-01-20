#falling skies game

import turtle
import time
import random
import winsound

#set the delay
delay = 0.015

#score the game
score = 0

#lives
lives = 10

#set up the screen
wn = turtle.Screen()
wn.title("Falling Skies Game")
wn.bgcolor("black")
wn.bgpic("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Falling_Skies/background.gif")
wn.setup(width=800, height=600)
wn.tracer(0)

#register images
wn.register_shape("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Falling_Skies/deer.gif")

#add the player
player = turtle.Turtle()
player.speed(0)
player.shape("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Falling_Skies/deer.gif")
player.color("white")
player.penup()
player.goto(0, -250)
#at the start of the game the player is not moving
player.direction = "stop"

#create a list of good guys
good_guys = []

#add the good guys
for _ in range(10): #number of good guys
	good_guy = turtle.Turtle()
	good_guy.speed(0)
	good_guy.shape("circle")
	good_guy.color("blue")
	good_guy.penup()
	good_guy.goto(-100, 250)
	good_guy.speed = random.randint(1, 4)
	good_guys.append(good_guy)

#create a list of good guys
bad_guys = []

#add the bad guys #number of bad guys
for _ in range(10):
	bad_guy = turtle.Turtle()
	bad_guy.speed(0)
	bad_guy.shape("circle")
	bad_guy.color("red")
	bad_guy.penup()
	bad_guy.goto(100, 250)
	bad_guy.speed = random.randint(1, 4)
	bad_guys.append(bad_guy)

#create a pen
pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.goto(0, 260)
font = ("Courier", 24, "normal")
pen.write("Score: {} | Lives: {}".format(score, lives), align="center", font=font)

#functions
def go_left():
	player.direction = "left"
def go_right():
	player.direction = "right"

#keyboard binding
wn.listen()
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

#main game loop
while True:
	#update scree
	wn.update()
	#move the player
	if player.direction == "left":
		x = player.xcor()
		x -= 3
		player.setx(x)

	if player.direction == "right":
		x = player.xcor()
		x += 3
		player.setx(x)

	#move the good guys
	for good_guy in good_guys:
		y = good_guy.ycor()
		y -= good_guy.speed
		good_guy.sety(y)

		#check if off the screen
		if y < -300:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			good_guy.goto(x, y)
		#check for a collision with the player
		if good_guy.distance(player) < 20:
			winsound.PlaySound("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Falling_Skies/sound11.wav", winsound.SND_ASYNC)
			good_guy.goto(x, y)
			score += 10
			pen.clear()
			pen.write("Score: {} | Lives: {}".format(score, lives), align="center", font=font)

	#move the bad guys
	for bad_guy in bad_guys:
		y = bad_guy.ycor()
		y -= bad_guy.speed
		bad_guy.sety(y)

		#check if off the screen
		if y < -300:
			x = random.randint(-380, 380)
			y = random.randint(300, 400)
			bad_guy.goto(x, y)
		#check for a collision with the player
		if bad_guy.distance(player) < 20:
			bad_guy.goto(x, y)
			score -= 10
			lives -= 1
			pen.clear()
			pen.write("Score: {} | Lives: {}".format(score, lives), align="center", font=font)

	time.sleep(delay)

wn.mainloop()