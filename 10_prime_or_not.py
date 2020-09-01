'''
by Anshul Verma
19/78065

Write a function that takes a number as an input and determine whether it is prime or 
not.
'''
import math

def isPrime(n):
	if n <= 1:
		return False
	if n == 2 or n == 3:
		return True
	for i in range(2, int(math.sqrt(n))+1):
		if n%i == 0: return False;
	return True
	
print("5:", isPrime(5))
print("15:", isPrime(15))
print("97:", isPrime(97))
print("9864479961886:", isPrime(9864479961886))
print("7372838383147963:", isPrime(7372838383147963))