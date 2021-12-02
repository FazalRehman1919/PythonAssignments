"""Q:1. Make a calculator using Python with addition , subtraction ,
multiplication ,division and power."""


def addition(num1, num2):
    return num1 + num2


def subtraction(num1, num2):
    return num1 - num2


def multiplication(num1, num2):
    return num1 * num2


def division(num1, num2):
    return num1 / num2


def raise_to_the_power(num1, num2):
    return num1 ** num2


print("Select the operation")
print("1: For Addition")
print("2: For Subtraction")
print("3: For Multiplication")
print("4: For Division")
print("5: For Raise_to_the_Power")

while True:
    choice = input("Enter your choice for Operation: ")

    if choice in ('1', '2', '3', '4', '5'):
        num12 = float(input("Enter 1st number: "))
        num21 = float(input("Enter 2nd number: "))

        if choice == '1':
            print("The addition of ", num12, "and", num21, "is", addition(num12, num21))
        elif choice == '2':
            print("The Subtraction of ", num12, "and", num21, "is", subtraction(num12, num21))
        elif choice == '3':
            print("The Multiplication of ", num12, "and", num21, "is", multiplication(num12, num21))
        elif choice == '4':
            print("The Division of ", num12, "and", num21, "is", division(num12, num21))
        elif choice == '5':
            print("The ", num12, "Power of", num21, "is", raise_to_the_power(num12, num21))

        next_calculation = input("Let's Do Next Calculation: (Yes/No): ")
        if next_calculation == 'no':
            break
    else:
        print("Invalid Input!")

"""Q:2.. Write a program to check if there is any numeric value in list using for loop"""
lst1 = ["Babar", 90, "Shahad", "le", 209]
for i in lst1:
    if type(i) == int:
        print(i)


"""Q:3. Write a Python script to add a key to a dictionary."""
dict1 = {"Name": "Ahad", "rollNo": "12", "Department": "Computer Science"}
dict1["University"] = "UOP"
print(dict1)

"""Q:4.Write a Python program to sum all the numeric items in a dictionary."""
my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
print(sum(my_dict.values()))


"""Q:5.Write a program to identify duplicate values from list"""
list1 = [1, 2, 3, 4, 5, 2, 3, 4, 7, 9, 5]
list2 = []
for i in list1:
    if i not in list2:
        list2.append(i)
    else:
        print(i, end=' ')


"""Q:6.Write a Python script to check if a given key already exists in a dictionary"""
dict1 = {"Name": 23, "rollNo": 12, "Department": 45}


def check_dictionary(y):
    if y in dict1:
        print("\nKey is present")
    else:
        print("\nKey is not found!")


check_dictionary(23)