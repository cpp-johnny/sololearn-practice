numbers = range(10)

"""
By default, it starts from 0, increments by 1 and stops before the specified number.

The following code generates a list containing all of the integers, up to 10.
"""

# How many numbers does the following range generate?
# ans: 5

x = range(5)
# 0,1,2,3,4

numbers = list(range(10))
print(numbers)
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

numbers = list(range(3, 8))
print(numbers)
# [3, 4, 5, 6, 7]

print(range(20) == range(0, 20))
# True


#There’s also a third argument you can use with range(), and it’s really useful. It’s called Step and it determines the interval of the sequence produced. Take a look:
numbers = list(range(5, 20, 2))
print(numbers)
# [5, 7, 9, 11, 13, 15, 17, 19]

numbers = list(range(5, 20, 3))
print(numbers)
# [5, 8, 11, 14, 17]

# go backwards:
x = list(range(7, 3, -1))
print(x)
# [7, 6, 5, 4]


# You can use ranges in for loops, without the need to convert them into lists. 
# It’s commonly used to repeat some code a certain number of times. Like this:
for i in range(5):
  print("hello!")

"""
hello!
hello!
hello!
hello!
hello!
""" 

# only output even numbers from 0 to 20
for i in range(0, 20, 2):
  print(i)








