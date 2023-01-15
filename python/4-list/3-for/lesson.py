nums = [1, 2, 3, 4]

res = 0

for x in nums:

    if x % 2 == 0:

        continue
    else:
        res += x

print(res)


"""
This code defines a list of numbers called "nums" and a variable "res" that is initially set to 0. It then iterates through each number in the list "nums" using a for loop. For each iteration, it checks if the current number (x) is even (i.e. x%2==0) using an if statement. If the number is even, the loop continues to the next iteration using the "continue" statement. If the number is odd, the "res" variable is incremented by the value of x using the "res += x" statement. Finally, the code prints the final value of "res" which will be the sum of all odd numbers in the list "nums".

The output for the above code would be 4 because the list nums contains [1,2,3,4], out of these numbers 1 and 3 are odd numbers, and the sum of 1 and 3 is 4.

"""
