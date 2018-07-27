# Exercise 3-1
# Create a function that will accept a string and print enough leading spaces so that the last letter of the string is in column 70 of the display. 
def right_justify(s):
	string_length = len(s)
	space_length = 70 - string_length
	print(" " * space_length + s)

right_justify("monty")

# Exercise 3-2: displays how you can pass functions as an argument
def do_twice(f, value):
	f(value)
	f(value)

def print_twice(arg):
	print(arg)
	print(arg)

def do_four(f, value):
	do_twice(f, value)
	do_twice(f, value)

do_twice(print_twice, "spam")
print("   ")
do_four(print_twice, "spam")

# Exercise 3-3: print the shape shown in the book
def print_grid():
	print("+ " + ("- " * 4) + "+ " + ("- " * 4) + "+")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("+ " + ("- " * 4) + "+ " + ("- " * 4) + "+")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("|" + (" " * 9) + "|" + (" " * 9) + "|")
	print("+ " + ("- " * 4) + "+ " + ("- " * 4) + "+")

print_grid()