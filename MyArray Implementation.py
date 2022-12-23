from MyArray import Array
import random

myarray = Array(10)
print("My Array length is: ", len(myarray))
for i in range(len(myarray)):
    item = random.randint(0,9)
    myarray[i] = item
    print("{} --> {:.2f}".format(i,item))

print("My Array initialized upto {} values".format(len(myarray)))
aindex = int(input("Enter the index value of array element: "))

print("The array index {} contain items {}".format(aindex,myarray[aindex]))