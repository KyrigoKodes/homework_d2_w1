# 1. Decisions at the Crossroad
# Task 1: Code Correction
# You are provided with a Python script that uses conditional statements to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# Buggy Code:

number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# 2. The Greatest Showdown
# Objective: Harness the power of conditional statements to compare and determine values.
# Task 1: Identify the Greatest Write a Python program that prompts the user to enter three numbers. 
#The program should then identify and print out the largest number among the three.
first_int = int(input("Enter the first number: "))
second_int = int(input("Enter the second number: "))
third_int = int(input("Enter the third number: "))
largest = max(first_int, second_int, third_int)
print(f"The largest number is {largest}.")

# Task 2: Identify the Smallest Extend your program from Task 1 to also determine the smallest number 
#among the three and print it out.
print(f"The smallest number is {min(first_int, second_int, third_int)}.")

# Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that "The smallest number is 3. The largest number is 4."