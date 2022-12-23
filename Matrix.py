from Array2D import Array2D

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

    def scaleBy(self,scalar):
        for r in range(self.numRows()):
            for c in range(self.numCols()):
                self[r,c] *= scalar

    def transpose(self):
        newMatrix = Matrix(self.numRows(),self.numCols())
        for i in range(self.numCols):
            for j in range(self.numRows):
                newMatrix[i][j] = self[j][i]

    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows()and\
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation."
                # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows()):
            for c in range( self.numCols()):
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]
                return newMatrix

    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows()and\
            rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the sub operation."
                # Create the new matrix.
        newMatrix = Matrix( self.numRows(), self.numCols())
        # Add the corresponding elements in the two matrices.
        for r in range( self.numRows()):
            for c in range( self.numCols()):
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]
                return newMatrix

    def multiply(self, rhsMatrix):
        assert rhsMatrix.numRows() == self.numCols() , "Matrix sizes not compatible for the multiply operation."
        result = []
        for r in range(self.numRows):
            u = []
            for s in range(rhsMatrix.numCols):
                u.append(int(0))
            result.append(u)

        for r in range(self.numRows):
            for s in range(rhsMatrix.numCols):
                result[r][s]
        print("\nResult is: \n")
         # iterate through rows of r1
        for x in range(len(self)):
            # iterate through columns of c2
            for y in range(len(rhsMatrix[0])):
                # iterate through rows of r2
                for z in range(len(rhsMatrix)):
                    result[x][y] += self[x][z] * rhsMatrix[z][y]
        for r in result:
            print(r)
