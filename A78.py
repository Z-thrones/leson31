import array as arr
#Imporing the module
my_array = arr.array('i', [1, 3 , 5 , 3 , 7 , 9 , 3])
print("Original array:" + str(my_array))
#Making and printing the array
print("Number of occurence of 3 in said array:")
print(my_array.count(3))
#counting the number of occurences of 3
my_array.reverse()
print("Reverse order of the items")
print(str(my_array))
# Reversing the array