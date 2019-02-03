#Space Invaders

import turtle
import os
import math
import random
import winsound

#setting up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("The Space Invaders")
wn.setup(width=700, height=700) #screen size
wn.bgpic("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/bg_si.gif")

#register the shapes
turtle.register_shape("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/invader.gif")
turtle.register_shape("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/player.gif")

#draw the border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()
border_pen.setposition(-300, -300)
border_pen.pendown()
border_pen.pensize(3)

for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()

#set the score to 0
score = 0

#draw score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14))
score_pen.hideturtle()

#create the player
player = turtle.Turtle()
player.color("blue")
player.shape("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#choose a number of enemies
number_of_enemies = 5
#create a list of enemies
enemies = []

#add enemies to the list
for i in range(number_of_enemies):
#create the enemy
	enemies.append(turtle.Turtle())
for enemy in enemies:
	enemy.color("red")
	enemy.shape("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)

enemyspeed = 2

#create the player's missile
missile = turtle.Turtle()
missile.color("yellow")
missile.shape("triangle")
missile.penup()
missile.speed(0)
missile.setheading(90)
missile.shapesize(0.5, 0.5)
missile.hideturtle()

missilespeed = 20

#define missile state
#ready: ready to fire
#fire: missile is off
missilestate = "ready"

#move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
def move_right():
	x = player.xcor()
	x += playerspeed
	if x > +280:
		x = + 280	
	player.setx(x)

def fire_missile():
	global missilestate
	if missilestate == "ready":
		winsound.PlaySound("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/laser.wav", winsound.SND_ASYNC)
		missilestate = "fire"
	#move the missile above the player
	x = player.xcor()
	y = player.ycor()
	missile.setposition(x, y+10)
	missile.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(), 2) + math.pow(t1.ycor()-t2.ycor(), 2))
	if distance < 15:
		return True
#create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_missile, "space")

#main game loop
while True:

	for enemy in enemies:
		#move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#move the enemy back and down
		if enemy.xcor() > 280:
			#move all enemies down
			for e in enemies:
				y = e.ycor() 
				y -= 40
				e.sety(y)
			#change enemy direction
			enemyspeed *= -1
		
		if enemy.xcor() < -280:
			#move all enemies down
			for e in enemies:
				y = e.ycor() 
				y -= 40
				e.sety(y)
			#change enemy direction
			enemyspeed *= -1
			
		#checking for collision between missile and enemy
		if isCollision(missile, enemy):
			winsound.PlaySound("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/explosion.wav", winsound.SND_ASYNC)
			#reset the missile
			missile.hideturtle()
			missilestate = "ready"
			missile.setposition(0, -400)
			#reset the enemy
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#update score
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14))

		if isCollision(player, enemy):
			winsound.PlaySound("C:/Users/Усман/Documents/Usman Docs/Projects/Python/Space_Invaders/explosion.wav", winsound.SND_ASYNC)
			player.hideturtle()
			enemy.hideturtle()
			print("Start Again")
			break

	#fire the missile
	if missilestate == "fire":
		y = missile.ycor()
		y += missilespeed
		missile.sety(y)

	#checking the missile top position
	if missile.ycor() > 275:
		missile.hideturtle()
		missilestate = "ready"
