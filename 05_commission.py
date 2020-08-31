"""
by Anshul Verma
19/78065

Consider a showroom of electronic products, where there are various salesmen. Each salesman is given a commission of 5%, depending on the sales made per month. 
In case the sale done is less than 50000, then the salesman is not given any commission. 
Write a function to calculate total sales of a salesman in a month, commission and remarks for the salesman. 
Sales done by each salesman per week is to be provided as input. 

Assign remarks according to the following criteria:

	Excellent: Sales >=80000

	Good: Sales>=60000 and <80000

	Average: Sales>=40000 and <60000

	Work Hard: Sales < 40000
"""

def calc(sales):
	total_sales = 4*sales
	com_amt = 0
	if total_sales >= 50000:
		com_amt = total_sales*0.05
	remarks = None
	if total_sales >= 80000: 
		remarks = "Excellent"
	elif total_sales >= 60000:
		remarks = "Good"
	elif total_sales >= 40000:
		remarks = "Average"
	elif total_sales < 40000:
		remarks = "Work Hard"
	
	return total_sales, com_amt, remarks
		
sales = int(input("Enter the sales per week: "))
t_sales, com, rem = calc(sales)
print("\nTotal Sales:", t_sales)
print("Commission:", com)
print("Remarks:", rem)