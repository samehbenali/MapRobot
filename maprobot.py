import turtle
import time
import sys
from collections import deque

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("map robot atast club mahdia")
wn.setup(1300,700)

class Maze(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("square")
		self.color("white")
		self.penup()
		self.speed(0)

class sprite(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("turtle")
        self.color("red")
        self.setheading(270)
        self.penup()
        self.speed(0)
    def spriteup(self):
        self.setheading(90)
        self.forward(24)
    def spritedown(self):
        self.setheading(270)
        self.forward(24)
    def spriteleft(self):
        self.setheading(180)
        self.forward(24)
    def spriteright(self):
        self.setheading(0)
        self.forward(24)

class Green(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

grid = [
"+++++++++++++++++++",
"+         +       +",
"+ ++      +       +",
"+  +              +",
"+ s+      +       +",
"+++++ +++++++ +++++",
"+       +         +",
"+       +      e  +",
"+       +         +",
"+       +         +",
"+++++++++++++++++++",
]

def setup_maze(grid):
	global start_x, start_y, end_x, end_y
	for y in range(len(grid)):
		for x in range(len(grid[y])):
			character = grid[y][x]
			screen_x = -588 + (x * 24)
			screen_y = 288 - (y * 24)
			if character == "+":
				maze.goto(screen_x, screen_y)
				maze.stamp()
                		walls.append((screen_x, screen_y))
            		if character == "e":
                		green.goto(screen_x, screen_y)
                		end_x, end_y = screen_x,screen_y
            		if character == "s":
                		start_x, start_y = screen_x, screen_y 
                		sprite.goto(screen_x, screen_y)
            		if character == " " or character == "e":
            			path.append((screen_x, screen_y))

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y
    while len(frontier) > 0:
    	time.sleep(0)
        x, y = frontier.popleft()
        if(x - 24, y) in path and (x - 24, y) not in visited:
        	cell = (x - 24, y)
        	solution[cell] = x, y
            	frontier.append(cell) 
            	visited.add((x-24, y)) 

        if (x, y - 24) in path and (x, y - 24) not in visited:
        	cell = (x, y - 24)
            	solution[cell] = x, y
            	frontier.append(cell)
            	visited.add((x, y - 24))

        if(x + 24, y) in path and (x + 24, y) not in visited:
        	cell = (x + 24, y)
            	solution[cell] = x, y
            	frontier.append(cell)
           	visited.add((x +24, y))

        if(x, y + 24) in path and (x, y + 24) not in visited:
        	cell = (x, y + 24)
            	solution[cell] = x, y
            	frontier.append(cell)
            	visited.add((x, y + 24))

def backRoute(x, y):
	while (x, y) != (start_x, start_y):
		route.append((x,y))
		x, y = solution[x, y]
	route.append((x,y))

def go_to_hell(route):
    for i in range(1,len(route)+1):
	    xc=sprite.xcor()
	    yc=sprite.ycor()
	    (x,y)=route[-i]
	    if(x>xc):
		sprite.spriteright()
	    elif(x<xc):
		sprite.spriteleft()
	    elif(y>yc):
		sprite.spriteup()
	    elif (y<yc):
		sprite.spritedown()
    time.sleep(0.02)

maze = Maze()
green = Green()
sprite = sprite()

walls = []
path = []
visited = set()
frontier = deque()
solution = {}
route=[]

setup_maze(grid)
search(start_x,start_y)
backRoute(end_x, end_y)
go_to_hell(route)
wn.exitonclick()
