# Write a short Python function, is multiple(n, m), that takes two integer values and
# returns True if 𝑛𝑛 is a multiple of 𝑚𝑚, that is, 𝑛𝑛 = 𝑚𝑚𝑚𝑚 for some integer 𝑖𝑖, and False
# otherwise.
def is_multiple(m,n):
    if n%m == 0:
        return True
    else:
        return False

# Write a short Python function, is even(k), that takes an integer value and returns
# True if 𝑘𝑘 is even, and False otherwise. However, your function cannot use the
# multiplication, modulo, or division operators.
def is_even(k):
    if k%2 == 0:
        return True
    else:
        return False

# Create a function EvenList that takes a parameter n to input n number from users
# and returns the list of only even numbers.
def EvenList(n):
    for i in n:
        if i % 2 == 0:
            print(i,end=",")

# Write a short Python function, minmax(data), that takes a sequence of one or more
# numbers, and returns the smallest and largest numbers, in the form of a tuple of length
# two. Do not use the built-in functions min or max in implementing your
# solution.
def minmax(data):
    largest = data[0]
    smallest = data[0]
    for item in data:
        if item > largest:
            largest = item
        elif item < smallest:
            smallest = item
    return smallest, largest

# Write a short Python function that takes a positive integer 𝑛𝑛 and returns the sum of the
# squares of all the positive integers smaller than 𝑛𝑛.
def sumsquares(n):

