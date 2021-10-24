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
# Write a python program which takes two inputs from user and print them addition
first_integer = int(input("Enter first integer: "))
second_integer = int(input("Enter second integer: "))
addition_of_integer = first_integer + second_integer
print("The addition of two integers is: ", addition_of_integer)

# Q: 7
"""Write a program which takes 5 inputs from user for different subject’s marks, total it
and generate mark sheet using grades ? """
maths_marks = int(input("Enter maths paper marks: "))
chemistry_marks = int(input("Enter chemistry paper marks: "))
physics_marks = int(input("Enter physics marks: "))
english_marks = int(input("Enter english marks: "))
urdu_marks = int(input("Enter urdu marks: "))
total_marks = maths_marks + chemistry_marks + physics_marks + english_marks + urdu_marks
percentage = total_marks * 100 / 500
print("You got ", percentage, "%")
if percentage > 80:
    print("Grade A")
elif 60 < percentage < 80:
    print("Grade B")
elif 33 < percentage < 60:
    print("Grade C")
else:
    print("You are fail! ")

# Q: 8
# Write a program which take input from user and identify that the given number is even or odd?
even_or_odd = int(input("Enter a number: "))
if even_or_odd % 2 == 0:
    print("The number is EVEN")
else:
    print("The number is ODD")

# Q: 9
# Write a program which print the length of the list?
list1 = [12, 34, 78, 43, 89, 94, 44, 15]
print("The length of list is: ", len(list1))

# Q: 10
# Write a Python program to sum all the numeric items in a list?
print("The sum of list is: ", sum(list1))

# Q: 11
# Write a Python program to get the largest number from a numeric list.
print("The Largest number in the list is: ", max(list1))

# Q: 12
"""Take a list, say for example this one:

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 Write a program that prints out all the elements of the list that are less than 5."""
list2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in list2:
    if i < 5:
        print(i)