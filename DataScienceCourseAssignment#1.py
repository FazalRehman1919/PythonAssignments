# Q: 1
"""1. Write a Python program to print the following string in a specific format (see the
output).
Twinkle, twinkle, little star,
       How I wonder what you are!
              Up above the world so high,
               Like a diamond in the sky.
Twinkle, twinkle, little star,
       How I wonder what you are"""

print("Twinkle, twinkle, little star \n", "       ", "How I wonder what you are! \n", "              ",
      "Up above the world so high \n", "              ", "Like a diamond in the sky \n",
      "Twinkle, twinkle little star \n", "         ", "How I wonder what you are!")

# Q: 2
# 2. Write a Python program to get the Python version you are using.
import sys

print("Python version")
print(sys.version)

# Q: 3
# Write a Python program to display the current date and time.
import datetime

x = datetime.datetime.now()
print("Current Date and Time is: ", x.strftime("%Y-%m-%d %H:%M:%S"))

# Q: 4
"""Write a Python program which accepts the radius of a circle from the user and compute
the area."""
radius_of_circle = int(input("Enter the radius of circle: "))
Area = 3.14 * (radius_of_circle * radius_of_circle)
print("The AREA of Circle is: ", Area)

# Q: 5
"""Write a Python program which accepts the user's first and last name and print them in
reverse order with a space between them."""
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print(first_name[::-1], last_name[::-1])

# Q: 6
# Write a python program which takes two inputs from user and print then addition
first_integer = int(input("Enter first integer: "))
second_integer = int(input("Enter second integer: "))
addition_of_integer = first_integer + second_integer
print("The addition of two integers is: ", addition_of_integer)