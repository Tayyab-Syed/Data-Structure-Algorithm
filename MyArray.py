import ctypes

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

class Array2D:
    def __init__(self , numRows , numCols):
        self._theRows = Array(numRows)
        for i in range(numRows):
            self._theRows[i] = Array(numCols)

    def numRows(self):
        return len(self._theRows)

    def numCols(self):
        return len(self._theRows[0])

    def clear(self, value):
        for row in range(self.numRows()):
            self._theRows[row].clear(value)

    def __getitem__(self , ndxTuple):
        assert len(ndxTuple) == 2, "Invalid number of Array subscripts."
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols() ,\
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        return the1dArray[col]

    def __setitem__(self, ndxTuple , value):
        assert len(ndxTuple) == 2, "Invalid no of array subscripts"
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
            and col >= 0 and col < self.numCols(), \
                "Array subscript out of range."
        the1dArray = self._theRows[row]
        the1dArray[col] = value

twoDArray = Array2D(3,3)
twoDArray.clear(0)

for i in range(twoDArray.numRows()):
    print(" ")
    for j in range(twoDArray.numCols()):
        twoDArray[i,j] = int(input("Enter Value %d %d = " %(i,j)))

print("Your 2D-Array is here: ")
for i in range(twoDArray.numRows()):
    print(" ")
    for j in range(twoDArray.numCols()):
        print(twoDArray[i,j], end = " ")

class Matrix:
    def __init__(self, numRows, numCols):
        self._theGrid = Array2D(numRows , numCols)
        self._theGrid.clear(0)

    def numRows(self):
        return self._theGrid.numRows()

    def numCols(self):
        return self._theGrid.numCols()

    def __getitem__(self, ndxTuple):
        return self._theGrid[ndxTuple[0],ndxTuple[1]]

    def __setitem__(self,ndxTuple,scalar):
        self._theGrid[ndxTuple[0],ndxTuple[1]] = scalar

    # def scaleBy9