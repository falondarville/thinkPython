
import turtle
bob = turtle.Turtle()

def square(t):
	for t in range(4):
	bob.fd(100)
	bob.lt(90)

square(bob)
turtle.mainloop()