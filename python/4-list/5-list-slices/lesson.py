"""
List slices allow you to get a part of the list using two colon-separated indices. 
This returns a new list containing all the values between the indices.

Remember that first digit starts from 0, and the [2:6] the `6` is not included, so only until 5
"""

# take the first two elements of the list:
list = ["a", "b", "c", "d"]
a = list[0:2]

# Non-first
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])   # [4, 9, 16, 25]
print(squares[3:8])   # [9, 16, 25, 36, 49]
print(squares[0:1])   # [0]

# Inclusive of first
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[:7])    # [0, 1, 4, 9, 16, 25, 36]

# Only show the ends
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[7:])    # [49, 64, 81]

"""
quiz: how many elements will the folliwing output?
Ans: 5
"""
sq = [0, 1, 4, 9, 16, 25, 36, 49, 64]
print(sq[4:])   # [16, 25, 36, 49, 64]

"""
Just like with ranges, your list slices can include a third number, 
representing the step, to include only alternate values in the slice. Like this:
"""
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[::2])   # [0, 4, 16, 36, 64]
print(squares[2:8:3])   # [4, 25]

sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])    # [1, 25, 81]

"""
Negative values can also be used in list slicing (as well as normal list indexing). 

Which means that when negative values are used for the first and second values in a 
slice (or a normal index), they count from the end of the list. Like this:
"""

squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[1:-1])  # [1, 4, 9, 16, 25, 36, 49, 64]
print(squares[2:-2])  # [4, 9, 16, 25, 36, 49]

# Using [::-1] as a slice is a common and idiomatic way to reverse a list.
nums = [5, 42, 7, 1, 0]
res = nums[::-1]
print(res)

# quiz: how many elements will be extracted from here?
# Ans: 3
names = [1,2,3,4,5]
print(names[1:-1])

"""
The list comprehension names contains numbers from 1 to 5.
The slice operator names[1:-1] is used to extract elements from the list names.
The slice goes from index 1 to index -1 (index of last element -1) and returns all elements in between [2, 3, 4].
It means it will return all elements except first and last element of the list, which are 1 and 5 in this case.
"""
