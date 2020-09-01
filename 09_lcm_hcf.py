'''
by Anshul Verma
19/78065

Write a function that takes two numbers as input parameters and returns their least common multiple and highest common factor.
'''

def lcm_hcf(n1, n2):
	hcf = 0
	lcm = 0
	prod = n1*n2
	while n1 != n2:
		if n1 > n2:
			n1 = n1 - n2
		if n2 > n1:
			n2 = n2 - n1
	hcf = n1
	lcm = int(prod/hcf)
	return lcm, hcf
	
num1 = int(input("\nEnter Number 1: "))
num2 = int(input("Enter Number 2: "))

lcm, hcf = lcm_hcf(num1,num2)
print("\nLCM:", lcm)
print("HCF:", hcf)