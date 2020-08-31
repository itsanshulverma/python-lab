#by Anshul Verma, 19/78065

#Write a Python function that takes a number as an input from the user and computes its factorial.

def factorial(n):
	if n == 1: return 1
	return n*factorial(n-1)
	
num = int(input("Enter the number: "))

print("\nFactorial:", factorial(num))