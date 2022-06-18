# Lists is one of the most important and basic data structure in Python
# Arrays are called as 'List' in Python and they are mutable unlike strings. 
# Lists are dynamic in Python so there is no overflow problem as memory is automatically allocated as the elements are added
# Let's consider a static list and implement functions on the list and determine their Time and Space Complexities

my_list = [3, 5, 56, 34, 23, 1, 10, 55]
print(f"The original given list is: {my_list}")

# Time complexity for appending an element to the end of the list is: O(1)
my_list.append(4) # adds the element at the end of the list
print(f"The latest list after appending \'4\' as an element is: {my_list}")

# Time complexity for removing the last element of the list is: O(1)
my_list.pop() # removes the last element of the list
print(f"The list after popping the last item is: {my_list}")

# Time complexity to remove specific element of the list is: O(n)
my_list.remove(56) # removes all instances of a specific element in the list
print(f"The list after removing all instances of a specific element \'56\' from is: {my_list}")

# Time complexity for returning index: O(n)
my_list.index(5) # returns the index of the specific element

# Time complexity for adding specific element in a specified index is: O(n)
my_list.insert(1,22) # inserting '22' in the first index of the list(in place of '5')
print(f"The list after the inserting of an element at a specific place is {my_list}")

# Time complexity for reversing a list is: O(n)
my_list.reverse() # returns the list in reversed order of elements
print(f"The list after the items are reversed are: {my_list}")

# Python by defaults uses Timsort which is combination of both Merge and Insertion sort
# Time complexity: O(n*log n)
sorted_list = my_list.sort() # Sorts the list but doesn't return the list in sorted order
print(f"The list after the sort function implemented is: {sorted_list}")

new_list = [1,2,3,9,8,7,6,5,4]

# Time complexity for extending a list is: O(k) , here 'k' is size of the new_list
my_list.extend(new_list) # returns the list with adding the elements of the new list along with old items of the list
print(f"The list after adding elements of the new list is :{my_list}")

# Time complexity of count an instance in the list is: O(n)
count = my_list.count(1) # returns the total number of occurance of the element in the list
print(f"The number of times the number \'1\' is present in the list is: {count} ")

# Time complexity for iteration of the list is: O(n)
for i in my_list:
    print(f"The elements present in the list are {i}")

# Time complexity for finding the length of the list
length_of_list = len(my_list)
print(f"The length of the list is: {length_of_list}")

'''
Lists also have slicing function
list[start:stop]  # items start through stop-1
list[start:]      # items start through the rest of the array
my_list[:stop]       # items from the beginning through stop-1
my_list[:]           # a copy of the whole array
There is also the step value, which can be used with any of the above:

a[start:stop:step] # start through not past stop, by step

The slicing operator [] is actually being used in the above code with a slice() object using the : notation (which is only valid within []),
i.e.: a[start:stop:step] is equivalent to: a[slice(start, stop, step)]
To skip specifying a given argument, one might use None, so that e.g. a[start:] is equivalent to a[slice(start, None)] or a[::-1] is equivalent to a[slice(None, None, -1)].
'''
print(f"The last item in the array is: {my_list[-1]}")    # last item in the array
print(f"The last three items in the array are: {my_list[-3:]}")   # last three items in the array
print(f"All items of the array except the last three are: {my_list[:-3]}")   # everything except the last three items

# Similarly, step may be a negative number:
print(f"All items of the array in the reverse order are: {my_list[::-1]}")    # all items in the array, reversed
print(f"The first two items of the array reversed are: {my_list[1::-1]}")   # the first two items, reversed
print(f"The last two items of the array reversed are: {my_list[:-3:-1]}")  # the last two items, reversed
print(f"Everything except the last two items reversed are: {my_list[-3::-1]}")  # everything except the last two items, reversed
