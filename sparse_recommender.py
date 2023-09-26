class SparseMatrix:

    # parameterized constructor


    def __init__(self, row=None, col=None):
        self.rowsize=None
        self.colsize=None

        # No-argument constructor (default constructor)
        if row is None and col is None:
            try:
                self.rowsize = int(input("enter the row size"))
                self.colsize = int(input("enter the col size"))
            except:
                print("please enter the integer values")
        else:
            self.rowsize = row
            self.colsize = col

        self.matrixdata = {}

    def set(self, row, col, value):
        try:

            #check for integer value for row
            if not isinstance(row, int):
                raise ValueError("row must be an integer")

            #check for row size

            if row > (self.rowsize-1):
                raise ValueError("entered row "+str(row)+" is greater than the provided row size "+str(self.rowsize))

            #check for column size

            if col > (self.colsize-1):
                raise ValueError("entered column "+str(col)+" is greater than the provided column size "+str(self.colsize))


            #check for type of value to integer or float
            if not (isinstance(value,(int,float))):
                raise ValueError("The given value should be integer or float")



            #check for integer value for column
            if not isinstance(col,int):
                raise ValueError("column must be an integer")

            #check for negative values for row and column
            if row < 0 or col < 0:
                raise ValueError("Row and column indices must be non-negative")

            if value != 0:
                self.matrixdata[(row, col)] = value
            else:
                raise ValueError("provide a non zero integer value")
        except Exception as e:
            #print(str(e))
            return str(e)


    def get(self, row, col):
        try:

            #check for negative values for row and column
            if row < 0 or col < 0:
                raise ValueError("Row and column indices must be non-negative")

            #check for integer value for row
            if not isinstance(row, int):
                raise ValueError("provide value for row must be an integer")

            #check for integer value for column
            if not isinstance(col,int):
                raise ValueError("provide value for column must be an integer")


            #check for elements in the matrix
            if len(self.matrixdata) == 0:
               raise ValueError("sparse matrix is empty, please insert the values in sparse matrix")

            #check for row size
            if row > (self.rowsize-1):
                raise ValueError("entered row is greater than row size")

            #check for column size

            if col > (self.colsize-1):
                raise ValueError("entered column is greater than column size")



            # returns  0 if the given row and col do not exit
            #elf.matrixdata.get((row, col), "Given Row and Column does not exist")
            return self.matrixdata.get((row, col), 0)
        except Exception as e:
            #print(str(e))
            return str(e)


    def recommend_movie(self, vector):

        try:

            #check for empty vector
            if len(vector) == 0:
                raise ValueError("Provided Vector is empty, please insert values")

            #check for integer and float elements in vector
            if not all(isinstance(x,(int,float))for x in vector):
                raise ValueError("Vector elements must be integer or float")

            # check for elements in the Sparse matrix
            if len(self.matrixdata) == 0:
               raise ValueError("sparse matrix is empty, please insert the values in sparse matrix")

            #check for size of the vector
            if not len(vector)==self.colsize:
                raise ValueError("row size(no of elements in the vector) of the vector must be equal to column size of the sparse matrix and column size is "+str(self.colsize))

            #creating list with 0 elemnts of size vector
            result = [0] * len(vector-1)

            for (row, col), value in self.matrixdata.items():
                result[row] += (value * vector[col])


            return result


        except Exception as e:
            return str(e)
            #print(str(e))





    def add_movie(self, new_matrix):
        try:

            # Check for instance of new Sparse Matrix
            if not isinstance(new_matrix,SparseMatrix):
                raise  ValueError("new sparse matrix must be an instance of class SparseMatrix")


            #check for elements in the matrix
            if len(self.matrixdata) == 0:
                raise ValueError("sparse matrix is empty, please insert the values in sparse matrix")


            #Check for row and column size matches the existing Sparse matrix
            if not (self.rowsize==new_matrix.rowsize and self.colsize == new_matrix.colsize):
                raise ValueError("row and col size must match with existing matrix")



            resultSparseMatrix =SparseMatrix(new_matrix.rowsize,new_matrix.colsize)



            # Add another sparse matrix to the current matrix
            x=0

            while(x<self.rowsize):

                y=0
                while(y<self.colsize):

                    resultvalue=self.matrixdata.get((x, y), 0)+new_matrix.get(x,y)
                    if resultvalue!=0:
                        resultSparseMatrix.set(x,y,resultvalue)
                    y=y+1
                x=x+1
            return resultSparseMatrix

        except Exception as e:
            return str(e)

    def to_dense(self):

        try:
            # check for elements in the Sparse matrix
            if len(self.matrixdata) == 0:
                raise ValueError("sparse matrix is empty, please insert the values in sparse matrix")


            # Convert the sparse matrix to a dense matrix and return it
            dense_matrix={}
            x=0
            while(x<self.rowsize):
                y=0
                while(y<self.colsize):
                    dense_matrix[(x, y)] = self.matrixdata.get((x, y), 0)
                    y=y+1
                x=x+1

            return dense_matrix
        except Exception as e:
            return str(e)





