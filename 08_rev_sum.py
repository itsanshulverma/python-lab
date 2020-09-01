'''
by Anshul Verma
19/78065

Write a function that takes a number with two or more digits as an input and finds its reverse and computes the sum of its digits.
'''

def rev_sum(n):
	rev_n = 0
	sum_n = 0
	while(n>0):
		dig = n%10;
		sum_n = sum_n + dig;
		rev_n = dig + rev_n*10;
		n = int(n/10)
	return rev_n, sum_n
	
num = int(input("\nEnter a number: "))
r_num, s_num = rev_sum(num)
print('\nReverse:', r_num)
print('Sum of digits:', s_num)