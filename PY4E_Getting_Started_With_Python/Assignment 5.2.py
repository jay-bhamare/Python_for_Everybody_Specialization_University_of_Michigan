#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jayvant
#
# Created:     08/04/2020
# Copyright:   (c) jayvant 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------

# Assignment 5.2
# Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'.
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and
# put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if (num == "done"):
        break
    try:
        num = int(num)
    except:
        print ("Invalid input")
        continue
    if smallest is None:
        smallest = num
    if num > largest :
        largest = num
    elif num < smallest :
        smallest = num

def check(largest,smallest):
    print ("Maximum is", int(largest))
    print ("Minimum is", int(smallest))

check(largest,smallest)