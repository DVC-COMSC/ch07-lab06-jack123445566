inputvalues = input('Enter all elements values: ').split()
numbers1 = list(map(int, inputvalues))
numbers2 = []
for i in range(len(numbers1)):
	numbers2.append(numbers1[len(numbers1)-1])
	numbers1.pop(len(numbers1)-1)
print(numbers2)


# The following line is the same as the for-loop
# numbers1 = list(map(int, numbers))

# print ("The original list: ", numbers1)


