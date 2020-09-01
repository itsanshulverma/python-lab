'''
by Anshul Verma
19/78065

Write a Python function to return nth terms of Fibonacci sequence.
'''

#Recursive
def f(n):
	if n <= 1:
		return 1
	return f(n-1) + f(n-2)
	
#Iterative
#def f(n):
#	pnum = 0
#	ppnum = None
#	cnum = 1
#	for i in range(n):
#		ppnum = pnum
#		pnum = cnum
#		cnum = pnum + ppnum
#	return cnum
	
num = int(input("\nEnter a number: "))
print(f"\n{num}th term in fibonacci series:",f(num))
	