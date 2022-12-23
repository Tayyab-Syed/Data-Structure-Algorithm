# Import ctype library of C Language
import ctypes

# Initialize Array Class
class Array:
    def __init__(self , size):
        assert size > 0, "Array size must be > 0"
        self._size = size
        PyArrayType = ctypes.py_object*size
        self._elements = PyArrayType()
        self.clear(None)

    def __len__(self):
        return self._size

    def __getitem__(self , index):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        return self._elements[ index ]

    def __setitem__(self , index , value):
        assert index >= 0 and index < len(self), "Array subscript out of range"
        self._elements[ index ]

    def clear(self , value):
        for i in range(len(self)):
            self._elements[i] = value
    
    def __iter__(self):
        return _ArrayIterator(self._elements)

class _ArrayIterator:
    def __init__(self , theArray):
        self._arrayRef = theArray
        self._curNdx = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self._curNdx < len(self._arrayRef):
            entry = self._arrayRef[self._arrayRef]
            self._curNdx += 1
            return entry
        else:
            raise StopIteration


# Array Implementation

# import random
# myarray = Array(10)
# print("My Array length is",len(myarray))
# for i in range(len(myarray)):
#     item = random.random()
#     print("{} --> {:2f}".format(i,item))
#     myarray[i] = item
# print("myrray initilized upto {} values".format(len(myarray)))
# aindex = int(input("Enter the index value of array element:" ))
# x = aindex
# print("The array index " + str(aindex) +" contains item "+ str(myarray[x]))
