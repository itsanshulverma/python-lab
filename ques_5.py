# Importing factorial function created previously
from ques_3 import factorial

# Function to find sum of given series
def sum_series(x, n):
    sum = 0
    for i in range(1, n+1, 1):
        term = x**(2*i-2)/factorial(2*i-2) #Calculating nth term
        if i % 2 == 0:
            sum -= term
        else:
            sum += term
    return sum

if __name__ == "__main__":
    n = int(input("Enter n: "))
    x = int(input("Enter x: "))
    sum = sum_series(x, n)
    print("Sum of {} terms for x={}: {}".format(n, x, sum))