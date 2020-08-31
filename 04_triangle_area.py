"""
by Anshul Verma
19/78065

4. Write a function that takes the lengths of three sides: 
side1, side2 and side3 of the triangle as the input from 
the user using input function and return the area of the 
triangle as the output. Also, assert that sum of the 
length of any two sides is greater than the third side.
"""
import math

def area(side1, side2, side3):
	area = -1
	if side1 + side2 > side3 and side2 + side3 > side1 and side1 + side3 > side2:
		s = (side1 + side2 + side3)/2
		area = math.sqrt(s*(s-side1)*(s-side2)*(s-side3))
	else:
		print("\nERR: Entered sides does not form a triangle.\n-> Sum of any two sides of a triangle is always greater than the third side.")
	return area

side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

if not area(side1, side2, side3) == -1: print('\nArea: ', area(side1, side2, side3))