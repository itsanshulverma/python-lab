# Check if all elements of list are numbers or not
def check_int(l):
	for i in range(0, len(l),1):
		if not l[i].isnumeric():
			return False
	return True

# If it is a numeric list, then count number of odd values
def count_odd(l):
	if check_int(l):
		count = 0
		for i in range(0,len(l),1):
			if int(l[i]) % 2 != 0:
				count += 1
		print("Count of odd numbers: ", count)

# If list contains all strings, then display largest string in the list	
def largest_str(l):
	flag = True
	for i in range(0, len(l), 1):
		if type(l[i]) != str:
			flag = False
			
	if flag:
		largest = l[0]
		for i in l:
			if len(i) > len(largest):
				largest = i
		print("Largest string: ", largest)
	else:
		print("List does not contain all strings!")	

# Display list in reverse form
def display_reverse(l):
	for i in range(len(l)-1, -1, -1):
		print(l[i], end=" ")

# Find a specific item in the list
def find_item(item, l):
	for i in range(0, len(l), 1):
		if item == l[i]:
			print("Item found at index: ", i)
			return
	print("Item not found")

# Remove the specified item in the list
def remove_item(item, l):
	for i in range(0, len(l), 1):
		if item == l[i]:
			l.remove(item)
			print("Item removed")
			return

# Sort the list in descending order
def sort_desc(l):
	return sorted(l, reverse=True)
	
# Accept two list and find common members in them
def common(l1, l2):
	common = []
	for i in range(0, len(l1), 1):
		for j in range(0, len(l2), 1):
			if l1[i] == l2[j]:
				common.append(l1[i])
	if common:
		print("Common elements: ", common)
	else:
		print("No common element")
	return

if __name__ == "__main__":
	l = []
	n = int(input("Enter the size of list: "))
	for i in range(0, n,1):
		l.append(input("Enter element: "))
		
	if check_int(l):
		print("All elements are numbers")
	else:
		print("All elements are not numbers")
	
	count_odd(l)
	
	largest_str(l)
	
	print("Reversed list:", end=" ")
	display_reverse(l)
	
	item = input("\nEnter an element: ")
	find_item(item,l)
	
	remove_item(item, l)
	
	print("Sorted in Descending Order: ")
	print(sort_desc(l))
	l2 = []
	n = int(input("Enter the size of new list: "))
	for i in range(0, n, 1):
		l2.append(input("Enter element: "))

	common(l, l2)
	