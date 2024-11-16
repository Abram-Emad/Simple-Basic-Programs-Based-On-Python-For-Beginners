# The Sum Of Two Numbers
print("The Sum Of Two Numbers")

# Prompt user to input the first number
x = eval(input("Please input the first number = "))

# Prompt user to input the second number
y = eval(input("Please input the second number = "))

# Calculate the sum of the two numbers
z = x + y

# Print the sum of the two numbers
print("The sum of {0} and {1} is equal to ".format(x, y), z)
print("---------------------------------------------------------")

# Calculation of the area of a triangle
print("Calculation of the area of triangle")

# Prompt user to input the height of the triangle
a = eval(input("Please input the height = "))

# Prompt user to input the base width of the triangle
b = eval(input("Please input the base width = "))

# Calculate the area of the triangle
c = 0.5 * a * b

# Print the area of the triangle
print("The area of triangle is equal to ", c)
print("---------------------------------------------------------")

# Swap of two variables
print("Swap of two variables")

# Prompt user to input the first variable
g = eval(input("Please input the first variable = "))

# Prompt user to input the second variable
h = eval(input("Please input the second variable = "))

# Swap the values of the two variables
g, h = h, g

# Print the swapped values
print("The first variable is equal to {0} and The second variable is equal to {1}".format(g, h))
print("---------------------------------------------------------")

# Determining if the number is even or odd
print("Determining if the number is even or odd")

# Prompt user to input a number
j = eval(input("Please input your number = "))

# Check if the number is even
if (j % 2 == 0):
    print("even")
# Otherwise, the number is odd
else:
    print("odd")
print("---------------------------------------------------------")

# Determining if a student is pass or fail based on grades
print("Determining if a student is pass or fail based on the grades")

# Prompt user to input the grades of four subjects
s1 = eval(input("Please input the grade of the first subject = "))
s2 = eval(input("Please input the grade of the second subject = "))
s3 = eval(input("Please input the grade of the third subject = "))
s4 = eval(input("Please input the grade of the fourth subject = "))

# Calculate the average grade
St = (s1 + s2 + s3 + s4) / 4

# Check if the average grade is less than 50
if St < 50:
    print("The Student fail")
# Otherwise, the student passes
else:
    print("The Student pass")
print("---------------------------------------------------------")

# Computing the roots of a quadratic equation
print("Computing the roots of a quadratic equation")

# Prompt user to input the values of coefficients a, b, and c
A = eval(input("Please input the value of a = "))
B = eval(input("Please input the value of b = "))
C = eval(input("Please input the value of c = "))

# Calculate the discriminant
d = (B**2) - (4*A*C)

# Check if the discriminant is positive
if d > 0:
    print("different roots")
    r1 = (-B + (d**0.5)) / (A * 2)
    r2 = (-B - (d**0.5)) / (A * 2)
    print(r1, r2)
# Check if the discriminant is negative
elif d < 0:
    print("complex roots")
    r1 = (-B + (d**0.5)) / (A * 2)
    r2 = (-B - (d**0.5)) / (A * 2)
    print(r1, r2)
# If the discriminant is zero
else:
    print("equal roots")
    r = B / (A * 2)
    print(r, r)
print("---------------------------------------------------------")

# Check the age of a person to determine if they are a child, young, old, or in their golden age
print("Checking the age of a person to determine if they are a child, young, old, or in their golden age")

# Prompt user to input their age
age = eval(input("Please Input Your age "))

# Determine the age category
if age > 0 and age < 18:
    print("You are still a child")
elif age >= 18 and age < 40:
    print("You are young")
elif age >= 40 and age < 60:
    print("You are becoming old")
elif age >= 60 and age < 100:
    print("You are in the golden age right now")
else:
    print("Invalid input")
print("-------------------------------------------------------------------------------------------")

# Check if a number is positive, negative, or zero
print("Checking if a number is positive, negative, or zero")

# Prompt user to input a number
num = eval(input("Please enter the number that you want to check "))

# Determine if the number is positive, negative, or zero
if num > 0:
    print("The number you entered is positive")
elif num < 0:
    print("The number you entered is negative")
elif num == 0:
    print("The number you entered is zero")
else:
    print("Invalid input")
print("-------------------------------------------------------------------------------------------")

# Check if a number is positive, negative, or zero using nested if
print("Checking if a number is positive, negative, or zero using nested if")

# Prompt user to input a number
num = eval(input("Please enter the number you want to check "))

# Determine if the number is positive, negative, or zero using nested if
if num >= 0:
    if num > 0:
        print("The number you entered is positive")
    elif num == 0:
        print("The number you entered is zero")
else:
    print("The number you entered is negative")
print("-------------------------------------------------------------------------------------------")

# Check whether a year is a leap year or not
print("Checking whether a year is a leap year or not")

# Prompt user to input a year
year = eval(input("Please input the year that you want to know if it's leap or not"))

# Determine if the year is a leap year
if year % 4 == 0:
    if year % 100 == 0:
       if year % 400 == 0:
           print("{0} is a leap year".format(year))
       else:
           print("Not a leap year")
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} isn't a leap year".format(year))
print("-------------------------------------------------------------------------------------------")

# Creating the multiplication table (from 1 to 12) of a number 'Using for Loop'
print("Creating the multiplication table (from 1 to 12) of a number 'Using for Loop'")
Number = int(input("Enter your Number = "))
for i in range(1, 13):
    print(Number, "*", i, "=", Number * i)
print("--------------------------------------------------------------------------------")

# Creating the multiplication table (from 1 to 12) of a number 'Using while Loop'
print("Creating the multiplication table (from 1 to 12) of a number 'Using while Loop'")
Number = int(input("Enter your Number = "))
i = 1
while i <= 12:
    print(Number, "*", i, "=", Number * i)
    i += 1
print("--------------------------------------------------------------------------------")

# Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) 'Using for Loop'
print("Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) 'Using for Loop'")
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
print("--------------------------------------------------------------------------------")

# Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) 'Using while Loop'
print("Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) 'Using while Loop'")
i = 1500
while i <= 2700:
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    i += 1
print("--------------------------------------------------------------------------------")

# Printing all the numbers from 0 to 6 except 3 and 6 'Using for Loop'
print("Printing all the numbers from 0 to 6 except 3 and 6 'Using for Loop'")
for i in range(6):
    if i == 3 or i == 6:
        continue
    print(i, end=",")
print("--------------------------------------------------------------------------------")

# Printing all the numbers from 0 to 6 except 3 and 6 'Using while Loop'
print("Printing all the numbers from 0 to 6 except 3 and 6 'Using while Loop'")
i = 0
while i < 6:
    if i != 3 and i != 6:
        print(i, end=",")
    i += 1
print("--------------------------------------------------------------------------------")

# The Fibonacci sequence between 0 and 50 'Using for Loop'
print("The Fibonacci sequence between 0 and 50 'Using for Loop'")
x, y = 0, 1
for _ in range(51):
    print(x)
    x, y = y, x + y
print("--------------------------------------------------------------------------------")

# The Fibonacci sequence between 0 and 50 'Using while Loop'
print("The Fibonacci sequence between 0 and 50 'Using while Loop'")
x, y = 0, 1
while x <= 50:
    print(x)
    x, y = y, x + y
print("--------------------------------------------------------------------------------")

# Finding even and odd numbers between 100 and 400 (both included) 'Using for Loop'
print("Finding even and odd numbers between 100 and 400 (both included) 'Using for Loop'")
for i in range(100, 401):
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
print("--------------------------------------------------------------------------------")

# Finding even and odd numbers between 100 and 400 (both included) 'Using while Loop'
print("Finding even and odd numbers between 100 and 400 (both included) 'Using while Loop'")
i = 100
while i <= 400:
    if i % 2 == 0:
        print(i, "is Even")
    else:
        print(i, "is Odd")
    i += 1
print("--------------------------------------------------------------------------------")

# Finding even and odd numbers between 100 and 400 (both included) 'Using for Loop' with another way
print("Finding even and odd numbers between 100 and 400 (both included) 'Using for Loop' with another way")
E, O = [], []
for i in range(100, 401):
    if i % 2 == 0:
        E.append(i)
    else:
        O.append(i)
print(E)
print(O)
print("--------------------------------------------------------------------------------")

# Finding even and odd numbers between 100 and 400 (both included) 'Using while Loop' with another way
print("Finding even and odd numbers between 100 and 400 (both included) 'Using while Loop' with another way")
E, O = [], []
i = 100
while i <= 400:
    if i % 2 == 0:
        E.append(i)
    else:
        O.append(i)
    i += 1
print(E)
print(O)
print("--------------------------------------------------------------------------------")

# Counting the number of even and odd numbers from a series of numbers 'Using for Loop'
print("Counting the number of even and odd numbers from a series of numbers 'Using for Loop'")
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
ce, co = 0, 0
for i in x:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
print("Even Count", ce)
print("Odd Count", co)
print("--------------------------------------------------------------------------------")

# Counting the number of even and odd numbers from a series of numbers 'Using while Loop'
print("Counting the number of even and odd numbers from a series of numbers 'Using while Loop'")
ce, co = 0, 0
i = 1
while i <= 9:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
    i += 1
print("Even Count", ce)
print("Odd Count", co)
print("--------------------------------------------------------------------------------")

# Printing solid rectangular star pattern 'Using For Loop'
print("Printing solid rectangular star pattern 'Using For Loop'")
Rows = 3
Columns = 5
for i in range(1, Rows + 1):
    for j in range(1, Columns + 1):
        print("*", end=' ')
    print("\n")
print("_______________________________________________________________")

# Printing solid square star pattern 'Using For Loop'
print("Printing solid square star pattern 'Using For Loop'")
Rows = 3
Columns = 3
for i in range(1, Rows + 1):
    for j in range(1, Columns + 1):
        print("*", end=' ')
    print("\n")
print("_______________________________________________________________")

# Printing solid left half pyramid star pattern 'Using For Loop'
print("Printing solid left half pyramid star pattern 'Using For Loop'")
Rows = 5
for i in range(1, Rows + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print("\n")
print("_______________________________________________________________")

# Printing solid left inverted half pyramid star pattern 'Using For Loop'
print("Printing solid left inverted half pyramid star pattern 'Using For Loop'")
Rows = 5
for i in range(Rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print("\n")
print("_______________________________________________________________")

# Printing solid right half pyramid star pattern 'Using For Loop'
print("Printing solid right half pyramid star pattern 'Using For Loop'")
Rows = 5
for i in range(1, Rows + 1):
    print((Rows - i) * ' ', i * '*')
print("_______________________________________________________________")

# Printing solid right inverted half pyramid star pattern 'Using For Loop'
print("Printing solid right inverted half pyramid star pattern 'Using For Loop'")
Rows = 5
for i in range(Rows, 0, -1):
    print((Rows - i) * ' ', i * '*')
print("_______________________________________________________________")

# Printing solid Double left half pyramids star pattern 'Using For Loop'
print("Printing solid Double left half pyramids star pattern 'Using For Loop'")
Rows = 5
for i in range(1, Rows + 1):
    for j in range(1, i + 1):
        print("*", end='')
    print((Rows - i) * ' ', i * '*')
print("_______________________________________________________________")

# Printing solid equilateral triangle star pattern 'Using For Loop'
print("Printing solid equilateral triangle star pattern 'Using For Loop'")
Rows = 7
m = (2 * Rows) - 2
for i in range(0, Rows):
    for j in range(0, m):
        print(end=" ")
    m = m - 1  # decrementing m after each loop
    for j in range(0, i + 1):
        # printing full Triangle pyramid using stars
        print("*", end=' ')
    print("\n")
print("_______________________________________________________________")

# Quiz Number 1
# 1. Determining if the number can be divided by 3
print("1. Determining if the number can be divided by 3")
Number = int(input("Enter Your Number = "))
if Number % 3 == 0:
    print("The number you entered is {0} and it can be divided by 3".format(Number))
else:
    print("The number you entered is {0} and it can't be divided by 3".format(Number))
print("-------------------------------------------------------------------------------------------")

# 2. One line code that displays 1&2&3&4
print("Write a one line code that display 1&2&3&4")
print(1, 2, 3, 4, sep='&')
print("-------------------------------------------------------------------------------------------")

# Quiz Number 2
# 1. Read a string from the user and if g print girl and if b print boy
print("Write a Python program to read a string from the user and if g print girl and if b print boy")
Type = input("If you are a boy, please enter b or B. If you are a girl, please enter g or G: ")
if Type in ("b", "B"):
    print("OK, you are a boy")
elif Type in ("g", "G"):
    print("OK, you are a girl")
else:
    print("Invalid Input")
print("-------------------------------------------------------------------------------------------")

# 2. One line code that displays 1*2*3*4*
print("Write a one line code that display 1*2*3*4*")
print(1, 2, 3, 4, sep='*', end='*')
print("-------------------------------------------------------------------------------------------")

# Quiz Number 3
# 1. Check if the number is 7 or not
print("Check if the number is 7 or not")
Number = eval(input("Enter Your Number = "))
if Number == 7:
    print("The number you entered is equal to 7")
else:
    print("The number you entered isn't equal to 7")
print("-------------------------------------------------------------------------------------------")

# 2. One line code that displays 1@2@3@4$
print("Write a one line code that display 1@2@3@4$")
print(1, 2, 3, 4, sep='@', end='$')
print("-------------------------------------------------------------------------------------------")

# Quiz Number 4
# 1. Check if the letter is H or not
print("Check if the letter is H or not")
Letter = input("Enter Your letter = ")
if Letter in ("h", "H"):
    print("The letter you entered is {0}".format(Letter))
else:
    print("The letter you entered isn't H")
print("-------------------------------------------------------------------------------------------")

# 2. For x=3 y=5, display (The result of 3 and 5) using .format
print("For x=3 y=5, display (The result of 3 and 5) using .format")
x, y = 3, 5
print("The result is {0} and {1}".format(x, y))
print("-------------------------------------------------------------------------------------------")

# Quiz Number 5
# 1. Read two numbers from the user and determine which is larger
print("Determine which of the numbers entered by the user is larger")
first = eval(input("Please enter your first number = "))
second = eval(input("Please enter your second number = "))
if first > second:
    print("{0} is the first number you entered and it is larger than {1}, the second number you entered".format(first, second))
elif second > first:
    print("{1} is the second number you entered and it is larger than {0}, the first number you entered".format(first, second))
else:
    print("The two numbers you entered are equal")
print("-------------------------------------------------------------------------------------------")

# 2. For x=3 y=5, display (The result of 3 and 5) using .format
print("For x=3 y=5, display (The result of 3 and 5) using .format")
x, y = 3, 5
print("The result is {1} and {0}".format(x, y))
print("-------------------------------------------------------------------------------------------")

# Quiz Number 6
# 1. Determine if the student passes or fails based on the score (above 60 pass, below 60 fail)
print("Determine if the student passes or fails based on the score (above 60 pass, below 60 fail)")
Score = eval(input("Please enter your score = "))
if Score >= 60:
    print("Your score is {0} and you pass".format(Score))
else:
    print("Your score is {0} and you fail".format(Score))
print("-------------------------------------------------------------------------------------------")

# 2. For x="Welcome" y=2021, display (Welcome 2021) using .format
print("For x='Welcome' y=2021, display (Welcome 2021) using .format")
x, y = "Welcome", 2021
print("{0} {1}".format(x, y))
print("-------------------------------------------------------------------------------------------")

# Quiz Number 7
# 1. Check if the number is less than 10 and larger than 3
print("Check if the number is less than 10 and larger than 3")
Number = eval(input("Enter Your Number = "))
if 3 < Number < 10:
    print("The number you entered is less than 10 and larger than 3")
else:
    print("The number you entered isn't less than 10 and larger than 3")
print("-------------------------------------------------------------------------------------------")

# 2. For x=3 y=2021, display (Happy 2021 for class 3) using .format
print("For x=3 y=2021, display (Happy 2021 for class 3) using .format")
x, y = 3, 2021
print("Happy {1} for class {0}".format(x, y))
print("-------------------------------------------------------------------------------------------")

# Welcoming the user
print("Welcoming the user")
name = input("Please enter your name: ")
print("Hello", name)
print("-----------------------------------------")

# The sum of two numbers
print("The sum of two numbers")
x = eval(input("Please enter the first number: "))
y = eval(input("Please enter the second number: "))
z = x + y
print("The sum of these two numbers is equal to ", z)
print("-----------------------------------------")

# The average of two numbers
print("The average of two numbers")
i = eval(input("Please enter the first number: "))
p = eval(input("Please enter the second number: "))
t = (i + p) / 2
print("The average of these two numbers is equal to ", t)
print("-----------------------------------------")

# Calculating the area of a triangle
print("Calculating the area of triangle")
o = eval(input("Please enter the height of the triangle: "))
n = eval(input("Please enter the length of the base of the triangle: "))
l = 0.5 * o * n
print("The area of the triangle is ", l)
print("-----------------------------------------")

# Describing how many digits the number consists of
print("Describing how many digits the number consists of")
c = int(eval(input("Input your number: ")))
if 0 < c < 10:
    print("Your number consists of one digit")
elif 10 < c < 100:
    print("Your number consists of two digits")
else:
    print("The number you entered is a big number")
print("-----------------------------------------")

# Checking if the number is even or odd
print("Checking if the number is even or odd")
q = eval(input("Input your number: "))
if q % 2 == 0:
    print("The number you entered is even")
else:
    print("The number you entered is odd")
print("-----------------------------------------")

# Describing the grade of the student
print("Describing the grade of the student")
w = eval(input("Please input your score: "))
if w >= 95:
    print("Your score is equivalent to A+")
elif w >= 90:
    print("Your score is equivalent to A")
elif w >= 80:
    print("Your score is equivalent to B")
elif w >= 70:
    print("Your score is equivalent to C")
elif w >= 60:
    print("Your score is equivalent to D")
elif w >= 50:
    print("Your score is equivalent to D-")
else:
    print("Your score is equivalent to F")
print("-----------------------------------------")

# Checking if the entered number is between 1 to 10
print("Checking if the entered number is between 1 to 10")
d = eval(input("Please enter any number you want: "))
if 1 <= d <= 10:
    print("The number you entered is: ", d)
else:
    print("The number you entered isn't between 1 to 10")
print("-----------------------------------------")

# Choosing between a group of given colors
print("Choosing between a group of given colors")
print("1. Red")
print("2. Orange")
print("3. Yellow")
print("4. Green")
choice = int(eval(input("Please enter the number of your favorite color from the given list: ")))
if choice == 1:
    print("Your choice is red")
elif choice == 2:
    print("Your choice is orange")
elif choice == 3:
    print("Your choice is yellow")
elif choice == 4:
    print("Your choice is green")
else:
    print("You made an invalid choice")
print("-----------------------------------------")

# Sum of two numbers
x = eval(input("Enter the first number: "))
y = eval(input("Enter the second number: "))
s = y + x
print("The sum of {0} and {1} is {2}".format(x, y, s))

# Calculate the area of a triangle
x = eval(input("Enter the height please: "))
y = eval(input("Enter the base length please: "))
a = 0.5 * x * y
print("The area is", a)

# Swap of two variables
x = eval(input("Enter the first number: "))
y = eval(input("Enter the second number: "))
x, y = y, x
print("The first number is {0} and the second number is {1}".format(x, y))

# Check if the number is even or odd
x = eval(input("Enter the number: "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")

# Determine if the student passes or fails
s1 = eval(input("Enter the first subject score: "))
s2 = eval(input("Enter the second subject score: "))
s3 = eval(input("Enter the third subject score: "))
s4 = eval(input("Enter the fourth subject score: "))
st = (s1 + s2 + s3 + s4) / 4
if st >= 50:
    print("Pass")
else:
    print("Fail")

# Computing the roots of a quadratic equation
a = eval(input("Enter a: "))
b = eval(input("Enter b: "))
c = eval(input("Enter c: "))
d = (b ** 2) - (4 * a * c)
if d > 0:
    print("Different roots")
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print(r1, r2)
elif d < 0:
    print("Complex roots")
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print(r1, r2)
else:
    print("Equal roots")
    r = -b / (2 * a)
    print(r, r)

# Check if the number can be divided by 3
x = eval(input("Enter the number: "))
if x % 3 == 0:
    print("Your number is {0} and can be divided by 3".format(x))
else:
    print("Your number is {0} and can't be divided by 3".format(x))

# Read a string from the user and if g print girl and if b print boy
x = input("Enter b or g: ")
if x in ("b", "B"):
    print("Boy")
elif x in ("g", "G"):
    print("Girl")
else:
    print("Invalid syntax")

# Check if the number is 7 or not
x = eval(input("Enter the number: "))
if x == 7:
    print("Equal to 7")
else:
    print("Not equal to 7")

# Check if the input is h
if x in ("h", "H"):
    print("The input is h")
else:
    print("The input isn't h")

# Read two numbers from the user and determine which is larger
x = eval(input("Enter the first number: "))
y = eval(input("Enter the second number: "))
if x > y:
    print("The first number is larger than the second number")
elif x < y:
    print("The first number is smaller than the second number")
else:
    print("The two numbers are equal")

# Determine if the student passes or fails based on total grade
x = eval(input("Enter your total grade: "))
if x < 50:
    print("Fail")
else:
    print("Pass")

# Check if the number is less than 10 and larger than 3
x = eval(input("Enter your number: "))
if 3 < x < 10:
    print("The number you entered is less than 10 and larger than 3")
else:
    if x <= 3:
        print("The number you entered is less than 10 and smaller than or equal to 3")
    else:
        print("The number you entered is larger than or equal to 10")

# Determine if you are young, a child, old, or in your golden age
x = eval(input("Enter your age: "))
if 0 < x < 18:
    print("Child")
elif 18 <= x < 40:
    print("Young")
elif 40 <= x < 60:
    print("Old")
elif 60 <= x < 100:
    print("Golden age")
else:
    print("Invalid input")

# Check if a number is positive, negative, or zero
x = eval(input("Enter your number: "))
if x > 0:
    print("Positive")
elif x < 0:
    print("Negative")
else:
    print("Equal to zero")

# Check if a number is positive, negative, or zero using nested if
x = eval(input("Enter your number: "))
if x >= 0:
    if x > 0:
        print("Positive")
    else:
        print("Equal to zero")
else:
    print("Negative")

# Check if a year is a leap year or not
x = eval(input("Enter the year: "))
if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Leap year")
        else:
            print("Not a leap year")
    else:
        print("Leap year")
else:
    print("Not a leap year")

# Welcoming the user
n = input("Enter your name: ")
print("Welcome", n)

# Calculate the average of two numbers
x = eval(input("Enter the first number (n1): "))
y = eval(input("Enter the second number (n2): "))
a = (x + y) / 2
print("The average is", a)

# Determine the number of digits in a number
x = eval(input("Enter a number: "))
if 0 < x < 10:
    print("One digit")
elif 10 <= x < 100:
    print("Two digits")
elif 100 <= x < 1000:
    print("Three digits")
else:
    print("Big number")

# Describe the GPA based on the score
x = eval(input("Enter your GPA: "))
if x >= 95:
    print("A+")
elif x >= 90:
    print("A")
elif x >= 85:
    print("A-")
elif x >= 80:
    print("B+")
elif x >= 75:
    print("B")
elif x >= 65:
    print("C+")
elif x >= 60:
    print("C")
elif x >= 50:
    print("D")
else:
    print("F")

# Check if the number is between 1 and 10
x = eval(input("Enter your number: "))
if 1 <= x <= 10:
    print("Between 1 and 10")
else:
    print("Not between 1 and 10")

# Choosing between a group of given colors
print("1. Red")
print("2. Orange")
print("3. Yellow")
print("4. Green")
c = int(input("Enter the number of the color you want from the list: "))
if c == 1:
    print("Red")
elif c == 2:
    print("Orange")
elif c == 3:
    print("Yellow")
elif c == 4:
    print("Green")
else:
    print("Invalid input")

# Multiplication table using for loop
x = eval(input("Enter the number for the table: "))
for i in range(1, 13):
    print(i, '*', x, '=', i * x)

# Multiplication table using while loop
x = eval(input("Enter the number for the table: "))
i = 1
while i <= 12:
    print(i, '*', x, '=', i * x)
    i += 1

# Finding numbers divisible by 7 and multiple of 5 between 1500 and 2700 using for loop
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Finding numbers divisible by 7 and multiple of 5 between 1500 and 2700 using while loop
i = 1500
while i <= 2700:
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    i += 1

# Printing all numbers from 0 to 6 except 3 and 6 using for loop
for i in range(6):
    if i == 3 or i == 6:
        continue
    print(i, end=',')

# Fibonacci sequence between 0 and 50 using for loop
x, y = 0, 1
for _ in range(50):
    print(y)
    x, y = y, x + y

# Finding even and odd numbers between 100 and 400 (both included) using for loop
for i in range(100, 401):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")

# Finding even and odd numbers between 100 and 400 (both included) using while loop
i = 100
while i <= 400:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    i += 1

# Finding even and odd numbers between 100 and 400 using list comprehension
e, o = [], []
for i in range(100, 401):
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
print(e, 'even')
print(o, 'odd')

# Finding even and odd numbers between 100 and 400 using while loop with lists
e, o = [], []
i = 100
while i <= 400:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
    i += 1
print(e, 'even')
print(o, 'odd')

# Counting even and odd numbers from a series of numbers using for loop
ce, co = 0, 0
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
for i in x:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
print(ce, 'even count')
print(co, 'odd count')

# Counting even and odd numbers from a series of numbers using while loop
ce, co = 0, 0
i = 1
while i <= 9:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
    i += 1
print(ce, 'even count')
print(co, 'odd count')

# Print "hello" 10 times using for loop
for i in range(10):
    print("hello")

# Calculating the average of 10 numbers using for loop
s = 0
for i in range(10):
    x = eval(input("Enter a number: "))
    s += x
print("The average is", s / 10)

# Calculating the sum of numbers from 1 to 100 using for loop
s = 0
for i in range(1, 101):
    s += i
print("The sum is", s)

# Calculating squares of numbers in a tuple using list comprehension
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
d = [i ** 2 for i in x]
print(d)

# Printing "artist abram" repeatedly in a while loop with decreasing rows
rows = 0
while rows > 6:
    print("artist abram" * rows)
    rows -= 1

# Converting temperature from Celsius to Fahrenheit repeatedly until -1000 is entered
temp = 0
while temp != -1000:
    temp = eval(input("Enter temperature in Celsius (-1000 to quit): "))
    print("Temperature in Fahrenheit:", ((9 / 5) * temp + 32))

# Printing solid rectangular star pattern using for loop
rows = 3
columns = 5
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print("*", end=' ')
    print('\n')

# Printing solid square star pattern using for loop
rows = 5
columns = 5
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print("*", end=' ')
    print('\n')

# Printing left half pyramid star pattern using for loop
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\n')

# Printing left inverted half pyramid star pattern using for loop
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\n')

# Printing right half pyramid star pattern using for loop
rows = 5
for i in range(1, rows + 1):
    print((rows - i) * ' ', i * "*")

# Printing right inverted half pyramid star pattern using for loop
rows = 5
for i in range(rows, 0, -1):
    print((rows - i) * ' ', i * "*")

# Calculating average of a given number of values
n = eval(input("Enter the number of values you want to calculate the average for: "))
s = 0
for i in range(n):
    num = eval(input("Enter a number: "))
    s += num
print('The average is', s / n)

# Calculating square roots of numbers in a list and finding the maximum value
d = [4, 9, 16]
x = [i ** 0.5 for i in d]
print('Square roots:', x)
print('Maximum value:', max(x))

# Printing solid rectangular star pattern
r = 3
c = 5
for i in range(1, r + 1):
    for j in range(1, c + 1):
        print('*', end=' ')
    print('\n')

# Printing solid square star pattern
r = 3
c = 3
for i in range(1, r + 1):
    for j in range(1, c + 1):
        print('*', end=' ')
    print('\n')

# Printing solid left half pyramid star pattern
r = 5
for i in range(1, r + 1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('\n')

# Printing solid left inverted half pyramid star pattern
r = 5
for i in range(r, 0, -1):
    for j in range(1, i + 1):
        print('*', end=' ')
    print('\n')

# Printing solid right half pyramid star pattern
r = 5
for i in range(1, r + 1):
    print((r - i) * ' ', i * '*')

# Printing solid right inverted half pyramid star pattern
r = 5
for i in range(r, 0, -1):
    print((r - i) * ' ', i * '*')

# Printing solid equilateral triangle star pattern
r = 50
m = (r * 2) - 2
for i in range(0, r):
    for j in range(0, m):
        print(end=' ')
    m = m - 1
    for j in range(1, i + 1):
        print('*', end=' ')
    print()

# Multiplication table using for loop
num = eval(input("Enter the number for the table: "))
for i in range(1, 13):
    print(num, "*", i, '=', i * num)

# Multiplication table using while loop
num = eval(input("Enter the number for the table: "))
i = 1
while i <= 12:
    print(num, "*", i, '=', i * num)
    i += 1

# Finding numbers divisible by 7 and multiple of 5 between 1500 and 2700 using for loop
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)

# Finding numbers divisible by 7 and multiple of 5 between 1500 and 2700 using while loop
i = 1500
while i <= 2700:
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    i += 1

# Printing all numbers from 0 to 6 except 3 and 6 using for loop
for i in range(6):
    if i == 3 or i == 6:
        continue
    print(i, end=",")

# Fibonacci sequence between 0 and 50 using for loop
x, y = 0, 1
for _ in range(50):
    print(y)
    x, y = y, x + y

# Finding even and odd numbers between 100 and 400 (both included) using for loop
for i in range(100, 401):
    if i % 2 == 0:
        print(i, 'even')
    else:
        print(i, 'odd')

# Finding even and odd numbers between 100 and 400 (both included) using while loop
i = 100
while i <= 400:
    if i % 2 == 0:
        print(i, 'even')
    else:
        print(i, 'odd')
    i += 1

# Finding even and odd numbers between 100 and 400 using lists
e, o = [], []
for i in range(100, 401):
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
print(e, 'even')
print(o, 'odd')

# Finding even and odd numbers between 100 and 400 using while loop with lists
e, o = [], []
i = 100
while i <= 400:
    if i % 2 == 0:
        e.append(i)
    else:
        o.append(i)
    i += 1
print(e, 'even')
print(o, 'odd')

# Counting even and odd numbers from a series of numbers using for loop
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
ce, co = 0, 0
for i in x:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
print(ce, 'even count')
print(co, 'odd count')

# Counting even and odd numbers from a series of numbers using while loop
ce, co = 0, 0
i = 1
while i <= 9:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
    i += 1
print(ce, 'even count')
print(co, 'odd count')

# Print "hello" 10 times using for loop
for i in range(10):
    print("hello")

# Calculating the average of 10 numbers using for loop
s = 0
for i in range(10):
    x = eval(input("Enter a number: "))
    s += x
print("The average is", s / 10)

# Calculating the sum of numbers from 1 to 100 using for loop
s = 0
for i in range(1, 101):
    s += i
print("The sum is", s)

# Calculating squares of numbers in a tuple using list comprehension
x = (1, 2, 3, 4, 5)
s = [i ** 2 for i in x]
print(s)

# Printing "abram" repeatedly in a while loop with decreasing rows
rows = 6
while rows > 0:
    print("abram" * rows)
    rows -= 1

# Converting temperature from Celsius to Fahrenheit repeatedly until -1000 is entered
temp = 0
while temp != -1000:
    temp = eval(input("Enter temperature (-1000 to quit): "))
    print("Temperature in Fahrenheit:", ((9 / 5) * temp + 32))

# Printing solid rectangular star pattern using for loop
rows = 3
columns = 5
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print("*", end=' ')
    print("\n")

# Printing solid square star pattern using for loop
rows = 5
columns = 5
for i in range(1, rows + 1):
    for j in range(1, columns + 1):
        print("*", end=' ')
    print("\n")

# Printing left half pyramid star pattern using for loop
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print("\n")

# Printing left inverted half pyramid star pattern using for loop
rows = 5
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print("\n")

# Printing right half pyramid star pattern using for loop
rows = 5
for i in range(1, rows + 1):
    print((rows - i) * " ", i * "*")

# Printing right inverted half pyramid star pattern using for loop
rows = 5
for i in range(rows, 0, -1):
    print((rows - i) * " ", i * "*")

# Printing equilateral triangle star pattern using for loop
rows = 10
m = (2 * rows) - 2
for i in range(0, rows):
    for j in range(0, m):
        print(end=' ')
    m = m - 1
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\n')

# Question 1: Printing solid left half pyramid star pattern
print('Q1')
Rows = 5
for i in range(1, Rows + 1):
    for j in range(1, i + 1):
        print("*", end=' ')
    print('\n')

# Question 2: Calculating the average of N numbers
print('Q2')
N = eval(input("Enter how many numbers do you want to calculate the average for: "))
s = 0
for i in range(N):
    num = eval(input("Enter a number: "))
    s += num
print("The average of the numbers you entered is", s / N)

# Question 3: Calculating the square roots of a list of numbers and finding the maximum value
print('Q3')
d = [4, 9, 16]
x = []
for i in d:
    x.append(i ** 0.5)
print('x =', x)
print(max(x))

# Question 5: Checking if a number is between 100 and 200
print('Q5')
x = eval(input("Enter a number: "))
if 100 < x < 200:
    print("{0} is the number that you entered and it is between 100 and 200".format(x))
else:
    print("{0} is the number that you entered and it isn't between 100 and 200".format(x))

# Calculating the area of a triangle
print("Calculating the area of a triangle")
height = eval(input("Please enter the height: "))
baselength = eval(input("Please enter the base length: "))
area = 0.5 * height * baselength
print("The area of the triangle =", area)
print("______________________________________________________________________")

# Calculating the sum of two numbers
print("Calculating the sum of two numbers")
firstnum = eval(input("Please enter the first number: "))
secondnum = eval(input("Please enter the second number: "))
Sum = firstnum + secondnum
print("The Sum of {0} and {1} is {2}".format(firstnum, secondnum, Sum))
print("______________________________________________________________________")

# Swapping two variables
print("Swapping two variables")
x = eval(input("Please enter the first number: "))
y = eval(input("Please enter the second number: "))
x, y = y, x
print("The first number is {0} and the second number is {1}".format(x, y))
print("______________________________________________________________________")

# Determining if the number is even or odd
print("Determining if the number is even or odd")
num = eval(input("Please enter the number you want to check: "))
if num % 2 == 0:
    print("The number you entered is {0} and it is an even number".format(num))
else:
    print("The number you entered is {0} and it is an odd number".format(num))
print("______________________________________________________________________")

# Determining if a student passes or fails based on the grades
print("Determining if a student passes or fails based on the grades")
s1 = eval(input("Please enter your first grade: "))
s2 = eval(input("Please enter your second grade: "))
s3 = eval(input("Please enter your third grade: "))
s4 = eval(input("Please enter your fourth grade: "))
st = (s1 + s2 + s3 + s4) / 4
if st < 50:
    print("Sorry, but you failed. Good luck next time!")
else:
    print("Congratulations, you passed!")
print("______________________________________________________________________")

# Computing the roots of a quadratic equation
print("Computing the roots of a quadratic equation")
a = eval(input("Please enter A: "))
b = eval(input("Please enter B: "))
c = eval(input("Please enter C: "))
d = (b ** 2) - (4 * a * c)
if d > 0:
    print("Different roots")
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print(r1, r2)
elif d < 0:
    print("Complex roots")
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print(r1, r2)
else:
    print("Equal roots")
    r = -b / (2 * a)
    print(r, r)
print("______________________________________________________________________")

# Determining if the number can be divided by 3
print("Determining if the number can be divided by 3")
num = eval(input("Please enter the number you want to check: "))
if num % 3 == 0:
    print("The number you entered is {0} and it can be divided by 3".format(num))
else:
    print("The number you entered is {0} and it can't be divided by 3".format(num))
print("______________________________________________________________________")

# Reading a string from the user and printing "girl" if it's 'g' and "boy" if it's 'b'
print("Reading a string from the user and printing 'girl' if it's 'g' and 'boy' if it's 'b'")
Type = input("If you are a girl, input 'G' or 'g'. If you are a boy, input 'B' or 'b': ")
if Type in ('b', 'B'):
    print("OK, you are a boy")
elif Type in ('g', 'G'):
    print("OK, you are a girl")
else:
    print("Invalid input")
print("______________________________________________________________________")

# Checking if the number is 7 or not
print("Checking if the number is 7 or not")
num = eval(input("Please enter the number you want to check: "))
if num == 7:
    print("The number you entered is {0} and it equals 7".format(num))
else:
    print("The number you entered is {0} and it doesn't equal 7".format(num))
print("______________________________________________________________________")

# Checking if the letter is 'H' or not
print("Checking if the letter is 'H' or not")
letter = input("Please enter the letter you want to check: ")
if letter in ('h', 'H'):
    print("The letter you entered is '{0}'".format(letter))
else:
    print("The letter you entered is '{0}' and it isn't 'H'".format(letter))
print("______________________________________________________________________")

# Determining which of the two numbers entered by the user is larger
print("Determining which of the two numbers entered by the user is larger")
firstnum = eval(input("Please enter the first number: "))
secondnum = eval(input("Please enter the second number: "))
if firstnum > secondnum:
    print("{0} is the first number you entered and it is larger than {1}".format(firstnum, secondnum))
elif firstnum < secondnum:
    print("{0} is the first number you entered and it is smaller than {1}".format(firstnum, secondnum))
else:
    print("The first number you entered equals the second number")
print("______________________________________________________________________")

# Determining if the student passes or fails depending on the score (above 60 passes, below 60 fails)
print("Determining if the student passes or fails depending on the score (above 60 passes, below 60 fails)")
Score = eval(input("Please enter your score: "))
if Score >= 60:
    print("Your score is {0} and you passed".format(Score))
else:
    print("Your score is {0} and you failed".format(Score))
print("______________________________________________________________________")

# Checking if the number is less than 10 and larger than 3
print("Checking if the number is less than 10 and larger than 3")
Number = eval(input("Enter your number: "))
if 3 < Number < 10:
    print("{0} is the number you entered and it is larger than 3 and less than 10".format(Number))
else:
    print("{0} is the number you entered and it isn't in the range of 3 to 10".format(Number))
print("______________________________________________________________________")

# Welcoming the user
print("Welcoming the user")
name = input("What's your name: ")
print('Hello', name, "How are you?")
print("______________________________________________________________________")

# Calculating the average of two numbers
print("Calculating the average of two numbers")
s1 = eval(input("Please enter your first variable: "))
s2 = eval(input("Please enter your second variable: "))
st = (s1 + s2) / 2
print("The average of the two numbers you entered is", st)
print("______________________________________________________________________")

# Describing how many digits the number consists of
print("Describing how many digits the number consists of")
c = int(eval(input("Input your number: ")))
if 0 < c < 10:
    print("{0} is the number you entered and it consists of one digit".format(c))
elif 10 <= c < 100:
    print("{0} is the number you entered and it consists of two digits".format(c))
elif 100 <= c < 1000:
    print("{0} is the number you entered and it consists of three digits".format(c))
else:
    print("{0} is the number you entered and it consists of more than three digits".format(c))
print("______________________________________________________________________")

# Describing the grade of the student
print("Describing the grade of the student")
w = eval(input("Please input your score: "))
if w >= 95:
    print("Your grade is equivalent to A+")
elif w >= 90:
    print("Your grade is equivalent to A")
elif w >= 85:
    print("Your grade is equivalent to A-")
elif w >= 80:
    print("Your grade is equivalent to B+")
elif w >= 75:
    print("Your grade is equivalent to B")
elif w >= 70:
    print("Your grade is equivalent to C+")
elif w >= 65:
    print("Your grade is equivalent to C")
elif w >= 60:
    print("Your grade is equivalent to D")
elif w >= 50:
    print("Your grade is equivalent to D-")
else:
    print("Sorry to tell you this bad news, but you failed")
print("______________________________________________________________________")

# Checking if the entered number is between 1 and 10
print("Checking if the entered number is between 1 and 10")
d = eval(input("Please enter any number you want: "))
if 1 <= d <= 10:
    print("{0} is the number you entered and it is between 1 and 10".format(d))
else:
    print("{0} is the number you entered and it isn't between 1 and 10".format(d))
print("______________________________________________________________________")
# Checking the age of a person to determine if they are a child, young, old, or in their golden age
print("Checking the age of a person to determine if they are a child, young, old, or in their golden age")
age = eval(input("Please input your age: "))
if 0 < age < 18:
    print("You are still a child")
elif 18 <= age < 40:
    print("You are still young")
elif 40 <= age < 60:
    print("You are old now")
elif 60 <= age < 100:
    print("You are in the golden age right now")
else:
    print("Invalid input")
print("______________________________________________________________________")

# Checking if a number is positive, negative, or zero
print("Checking if a number is positive, negative, or zero")
num = eval(input("Please enter the number you want to check: "))
if num > 0:
    print("The number you entered is positive")
elif num < 0:
    print("The number you entered is negative")
else:
    print("The number you entered is equal to zero")
print("______________________________________________________________________")

# Checking if a number is positive, negative, or zero with nested if
print("Checking if a number is positive, negative, or zero with nested if")
num = eval(input("Please enter the number you want to check: "))
if num >= 0:
    if num > 0:
        print("The number you entered is positive")
    elif num == 0:
        print("The number you entered is equal to zero")
else:
    print("The number you entered is negative")
print("______________________________________________________________________")

# Checking whether a year is a leap year or not
print("Checking whether a year is a leap year or not")
year = eval(input("Please input the year you want to check: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("{0} is a leap year".format(year))
        else:
            print("{0} is not a leap year".format(year))
    else:
        print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
print("______________________________________________________________________")

# Checking if values entered by the user (x and y) are larger than 5 using if condition
print("Checking if values entered by the user (x and y) are larger than 5 using if condition")
x = eval(input("Please enter the first number: "))
y = eval(input("Please enter the second number: "))
if x > 5 and y > 5:
    print("{0} and {1} are both larger than 5".format(x, y))
elif x < 5 and y < 5:
    print("{0} and {1} are both smaller than 5".format(x, y))
elif x > 5 and y < 5:
    print("{0} is larger than 5 but {1} is not".format(x, y))
elif x < 5 and y > 5:
    print("{0} is smaller than 5 but {1} is larger".format(x, y))
else:
    print("Both numbers are equal to 5")
print("______________________________________________________________________")

# Checking if values entered by the user (x and y) are larger than 5 using nested if
print("Checking if values entered by the user (x and y) are larger than 5 using nested if")
x = eval(input("Please enter the first number: "))
y = eval(input("Please enter the second number: "))
if x > 5:
    if y > 5:
        print("{0} and {1} are both larger than 5".format(x, y))
    else:
        print("{0} is larger than 5 but {1} is not".format(x, y))
else:
    print("{0} is smaller than 5".format(x))
print("______________________________________________________________________")

# Printing the color depending on the letter entered by the user (b means blue, y means yellow, etc.)
print("Printing the color depending on the letter entered by the user")
print("r or R: red")
print("o or O: orange")
print("y or Y: yellow")
print("g or G: green")
choice = input("Please enter the letter of your favourite color from the given list: ")
if choice in ('r', 'R'):
    print("You chose red")
elif choice in ('o', 'O'):
    print("You chose orange")
elif choice in ('y', 'Y'):
    print("You chose yellow")
elif choice in ('g', 'G'):
    print("You chose green")
else:
    print("Invalid input")
print("______________________________________________________________________")

# Creating the multiplication table (from 1 to 12) of a number using for loop
print("Creating the multiplication table (from 1 to 12) of a number using for loop")
number = eval(input("Enter the number for the multiplication table: "))
for i in range(1, 13):
    print(i, "*", number, "=", i * number)
print("______________________________________________________________________")
# Creating the multiplication table (from 1 to 12) of a number using while loop
print("Creating the multiplication table (from 1 to 12) of a number using while loop")
number = eval(input("Enter the number for the multiplication table: "))
i = 1
while i <= 12:
    print(i, "*", number, "=", i * number)
    i += 1
print("______________________________________________________________________")

# Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) using for loop
print("Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) using for loop")
for i in range(1500, 2701):
    if i % 7 == 0 and i % 5 == 0:
        print(i)
print("______________________________________________________________________")

# Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) using while loop
print("Finding those numbers which are divisible by 7 and multiple of 5, between 1500 and 2700 (both included) using while loop")
i = 1500
while i <= 2700:
    if i % 7 == 0 and i % 5 == 0:
        print(i)
    i += 1
print("______________________________________________________________________")

# Printing all the numbers from 0 to 6 except 3 and 6 using for loop
print("Printing all the numbers from 0 to 6 except 3 and 6 using for loop")
for i in range(6):
    if i == 6 or i == 3:
        continue
    print(i, end=',')
print("______________________________________________________________________")

# The Fibonacci sequence between 0 and 50 using for loop
print("The Fibonacci sequence between 0 and 50 using for loop")
x, y = 0, 1
for _ in range(51):
    print(y)
    x, y = y, x + y
print("______________________________________________________________________")

# Finding even and odd numbers between 100 and 400 (both included) using for loop
print("Finding even and odd numbers between 100 and 400 (both included) using for loop")
for i in range(100, 401):
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
print("______________________________________________________________________")

# Finding even and odd numbers between 100 and 400 (both included) using while loop
print("Finding even and odd numbers between 100 and 400 (both included) using while loop")
i = 100
while i <= 400:
    if i % 2 == 0:
        print(i, "is even")
    else:
        print(i, "is odd")
    i += 1
print("______________________________________________________________________")

# Finding even and odd numbers between 100 and 400 (both included) using for loop with another way
print("Finding even and odd numbers between 100 and 400 (both included) using for loop with another way")
E, O = [], []
for i in range(100, 401):
    if i % 2 == 0:
        E.append(i)
    else:
        O.append(i)
print(E, "are even")
print(O, "are odd")
print("______________________________________________________________________")

# Finding even and odd numbers between 100 and 400 (both included) using while loop with another way
print("Finding even and odd numbers between 100 and 400 (both included) using while loop with another way")
E, O = [], []
i = 100
while i <= 400:
    if i % 2 == 0:
        E.append(i)
    else:
        O.append(i)
    i += 1
print(E, "are even")
print(O, "are odd")
print("______________________________________________________________________")

# Counting the number of even and odd numbers from a series of numbers using for loop
print("Counting the number of even and odd numbers from a series of numbers using for loop")
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
ce, co = 0, 0
for i in x:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
print("Even count", ce)
print("Odd count", co)
print("______________________________________________________________________")

# Counting the number of even and odd numbers from a series of numbers using while loop
print("Counting the number of even and odd numbers from a series of numbers using while loop")
ce, co = 0, 0
i = 1
while i <= 9:
    if i % 2 == 0:
        ce += 1
    else:
        co += 1
    i += 1
print("Even count", ce)
print("Odd count", co)
print("______________________________________________________________________")

# Print "hello" ten times
print("Print 'hello' ten times")
for i in range(10):
    print("hello")
print("______________________________________________________________________")
# Asking the user to enter 10 numbers and calculating the average of them
print("Asking the user to enter 10 numbers and calculating the average of them")
s = 0
for i in range(10):
    num = eval(input("Enter a number: "))
    s += num
print("The average is", s / 10)
print("______________________________________________________________________")

# Adding numbers from 1 to 100
print("Adding numbers from 1 to 100")
s = 0
for i in range(1, 101):
    s += i
print("The sum is", s)
print("______________________________________________________________________")

# Squaring some numbers
print("Squaring some numbers")
x = (1, 2, 3, 4, 5, 6, 7, 8, 9)
s = [i ** 2 for i in x]
print(s)
print("______________________________________________________________________")

# Drawing a triangle of the word "Artist Abram"
print("Drawing a triangle of the word 'Artist Abram'")
Rows = 6
while Rows > 0:
    print("Artist Abram " * Rows)
    Rows -= 1
print("______________________________________________________________________")

# Changing the temperature from Celsius to Fahrenheit
temp = 0
while temp != -1000:
    temp = eval(input("Please input the temperature in Celsius (-1000 to quit): "))
    print("The temperature in Fahrenheit =", (9/5 * temp + 32))
print("______________________________________________________________________")

# Printing solid rectangular star pattern using for loop
print("Printing solid rectangular star pattern using for loop")
Rows = 3
Columns = 5
for i in range(1, Rows + 1):
    for j in range(1, Columns + 1):
        print("*", end=" ")
    print('\n')
print("______________________________________________________________________")

# Printing solid square star pattern using for loop
print("Printing solid square star pattern using for loop")
Rows = 5
Columns = 5
for i in range(1, Rows + 1):
    for j in range(1, Columns + 1):
        print("*", end=" ")
    print('\n')
print("______________________________________________________________________")

# Printing solid left half pyramid star pattern using for loop
print("Printing solid left half pyramid star pattern using for loop")
Rows = 5
for i in range(1, Rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('\n')
print("______________________________________________________________________")

# Printing solid left inverted half pyramid star pattern using for loop
print("Printing solid left inverted half pyramid star pattern using for loop")
Rows = 5
for i in range(Rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print('\n')
print("______________________________________________________________________")

# Printing solid right half pyramid star pattern using for loop
print("Printing solid right half pyramid star pattern using for loop")
Rows = 5
for i in range(1, Rows + 1):
    print((Rows - i) * " ", i * "*")
print("______________________________________________________________________")

# Printing solid right inverted half pyramid star pattern using for loop
print("Printing solid right inverted half pyramid star pattern using for loop")
Rows = 5
for i in range(Rows, 0, -1):
    print((Rows - i) * " ", i * "*")
print("______________________________________________________________________")

# Printing solid equilateral triangle star pattern using for loop
print("Printing solid equilateral triangle star pattern using for loop")
Rows = 7
m = (2 * Rows) - 2
for i in range(0, Rows):
    for j in range(0, m):
        print(end=' ')
    m -= 1
    for j in range(1, i + 1):
        print("*", end=" ")
    print('\n')
print("______________________________________________________________________")
