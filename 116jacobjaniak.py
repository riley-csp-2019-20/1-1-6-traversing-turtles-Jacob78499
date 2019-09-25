#   a116_traversing_turtles.py
#   Add code to make turtles move in a circle and change colors.
import turtle as trtl

# create an empty list of turtles
my_turtles = []

# use interesting shapes and colors
turtle_shapes = ["arrow", "turtle", "circle", "square", "triangle", "classic", "square", "circle","square","turtle"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold", "yellow", "blue", "brown", "blue","red"]

for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  new_color = turtle_colors.pop()
  t.speed(7)
  t.pensize(6)
  t.color(new_color)
  my_turtles.append(t)

# line 17 is for the starting point of each turtle 
startx = 0
starty = 0

# line 20 directs the turtles when they should move up a spot.
count = 1
for t in my_turtles:
	t.up()
	t.goto(startx, starty)
	t.right(45*count) 
	t.down()    
	t.forward(100)
	count += 1

#	line 27 gives them the exact location of where they should be.
	startx = t.xcor()
	starty = t.ycor()

wn = trtl.Screen()
wn.mainloop()