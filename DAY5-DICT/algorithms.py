import itertools

#Sorting an Array
a = [13, 5, 17, 9, 70, 43, 15]
a.sort()  # Sorts the list in ascending order in place
print(a)

#Sorting an Subarray
a = [13, 5, 17, 9, 70, 43, 15]
a[2:5] = sorted(a[2:5])  # Sorts the sublist from index 2 to 4
print(a)

#Sorting an Array in Reverse Order
a = [13, 5, 17, 9, 70, 43, 15]
a.sort(reverse=True)  # Sorts the list in descending order
print(a)

#Sorting an Array using Custom Sorting
arr = [(8, 4), (5, 2), (8, 6)]
arr.sort(key=lambda x: (x[0], -x[1]))  # Custom sorting using a lambda function
print(arr)


i = 5
print(bin(i).count('1'))

j = 987654321444333
print(bin(j).count('1'))



str = "bac"
# Sorting the string first
str = ''.join(sorted(str))

for perm in itertools.permutations(str):
    print(''.join(perm))


max_element = max(a)
print(max_element)