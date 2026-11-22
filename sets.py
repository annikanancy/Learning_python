#Creating a set(duplicates are automatically removed & are sorted)
numbers = {2, 3, 3, 4, 3, 4, 1}
print(numbers)

#Adding & Removing
numbers.add(5)
numbers.discard(2)
print(numbers)

#Checking whether a number is available or not in the set (fast membership testing)
print(2 in numbers)

#Mathematical Set Operations 
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a | b) #Union
print(a & b) #Intersection
print(a - b) #Difference
print(b - a)
print(a ^ b) #Symmetric Difference