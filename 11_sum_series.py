'''
by Anshul Verma
19/78065

Write a function that finds the sum of the n terms of the following series:

a) 1 – x²/2! + x⁴/4! – x⁶/6! + … x^n/n!
b) 1 + x²/2! + x⁴/4! + x⁶/6! + … x^n/n!
'''
import math

def sum_series(x, n):
	sum1 = 0
	sum2 = 0
	for i in range(1, n+1):
		term = math.pow(x,2*i - 2)/math.factorial(2*i - 2)
		sum2 += term
		if i%2 == 0: sum1 -= term
		else: sum1 += term
	return sum1, sum2			

sum1, sum2 = sum_series(7, 2)
print("Sum of Series 1:", sum1)
print("Sum of Series 2:", sum2)