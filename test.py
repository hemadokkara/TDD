import unittest
import sparse_recommender

class TestSparseMatrix(unittest.TestCase):
    def setUp(self):
        # Initialize a SparseMatrix for testing
        self.sparse_matrix = sparse_recommender.SparseMatrix(2,3)


    def test_set(self):

        try:

            # check to accept only  integers for row
            self.assertEqual(self.sparse_matrix.set("str",0,1),"row must be an integer")

            # check for integer value for column
            self.assertEqual(self.sparse_matrix.set(0,1.1,1),"column must be an integer")

            # check for negative values for row and column
            self.assertEqual(self.sparse_matrix.set(-1,-2,1),"Row and column indices must be non-negative")

            # test for incorrect row number
            self.assertEqual(self.sparse_matrix.set(3,0,1),"entered row "+str(3)+" is greater than the provided row size "+str(2))

            # test for incorrect col number
            self.assertEqual(self.sparse_matrix.set(0,3,1),"entered column "+str(3)+" is greater than the provided column size "+str(3))

            # check for type of value accepts  integer or float only
            self.assertEqual(self.sparse_matrix.set(0,0,"str"),"The given value should be integer or float")

            # check for non zero integer value
            self.assertEqual(self.sparse_matrix.set(0,0,0),"provide a non zero integer value")



            # test to set matrix values
            self.sparse_matrix.set(0, 0, 1)
            self.sparse_matrix.set(0, 1, 2)
            self.sparse_matrix.set(1, 1, 3)
            self.sparse_matrix.set(1, 2, 4)

        except Exception as e:
            print(str(e))

    def test_get(self):
        try:


            # check for empty sparse matrix
            self.assertEqual(self.sparse_matrix.get(0,0),"sparse matrix is empty, please insert the values in sparse matrix")

            # set the sparse matrix
            self.sparse_matrix.set(0, 0, 1)
            self.sparse_matrix.set(0, 1, 2)
            self.sparse_matrix.set(1, 1, 3)
            self.sparse_matrix.set(1, 2, 4)

            # check for row size
            self.assertEqual(self.sparse_matrix.get(3,4),"entered row is greater than row size")

            # check for column size
            self.assertEqual(self.sparse_matrix.get(0,4),"entered column is greater than column size")

            # check for integer value for row
            self.assertEqual(self.sparse_matrix.get(1.0,3),"provide value for row must be an integer")

            # check for integer value for column
            self.assertEqual(self.sparse_matrix.get(0,1.0),"provide value for column must be an integer")

            # check for negative values for row and column
            self.assertEqual(self.sparse_matrix.get(-2,0),"Row and column indices must be non-negative")
            self.assertEqual(self.sparse_matrix.get(0,-1),"Row and column indices must be non-negative")
            self.assertEqual(self.sparse_matrix.get(-1,-2),"Row and column indices must be non-negative")

            # returns 0 when Given Row and Column does not exist for zero elements in Sparse matrix
            self.assertEqual(self.sparse_matrix.get(0,2), 0)

            # test for all the inserted values
            self.assertEqual(self.sparse_matrix.get(0, 0), 1)
            self.assertEqual(self.sparse_matrix.get(0, 1), 2)
            self.assertEqual(self.sparse_matrix.get(1, 1), 3)
            self.assertEqual(self.sparse_matrix.get(1, 2), 4)


        except Exception as e:

            print(str(e))


    def test_recommend_movie(self):
        try:
            # test for empty vector
            self.assertEqual(self.sparse_matrix.recommend_movie([]), "Provided Vector is empty, please insert values")

            # check for elements in the matrix before multiplication
            self.assertEqual(self.sparse_matrix.recommend_movie([1,2,3,4]), "sparse matrix is empty, please insert the values in sparse matrix")

            # set the sparse matrix
            self.sparse_matrix.set(0, 0, 1)
            self.sparse_matrix.set(0, 1, 2)
            self.sparse_matrix.set(1, 1, 3)
            self.sparse_matrix.set(1, 2, 4)



            vector = ["str", True, -3, 1.1]

            # check for integer and float elements in vector
            self.assertEqual(self.sparse_matrix.recommend_movie(vector), "Vector elements must be integer or float")

            # Check for row and column size matches the existing Sparse matrix
            vector = [1, 1.1, 2, 3, 4.4]
            self.assertEqual(self.sparse_matrix.recommend_movie(vector), "row size(no of elements in the vector) of the vector must be equal to column size of the sparse matrix and column size is "+str(self.sparse_matrix.colsize))

            vector = [1, 2, 2, 1]
            self.assertEqual(self.sparse_matrix.recommend_movie(vector), "row size(no of elements in the vector) of the vector must be equal to column size of the sparse matrix and column size is "+str(self.sparse_matrix.colsize))

            # test for multiplication of vector and sparse matrix
            vector = [1, 2, 1]
            assert self.sparse_matrix.recommend_movie(vector) == [5,10]



        except Exception as e:
            print(str(e))

    def test_add_movie(self):
        try:

            # check for elements in new Sparse Matrix
            self.assertEqual(self.sparse_matrix.add_movie(sparse_recommender.SparseMatrix(2,3)), "sparse matrix is empty, please insert the values in sparse matrix")

            # check for instance of new Sparse Matrix
            self.assertEqual(self.sparse_matrix.add_movie({(1, 2): 3}), "new sparse matrix must be an instance of class SparseMatrix")


            newTestSparseMatrixObj = sparse_recommender.SparseMatrix(3,3)
            newTestSparseMatrixObj.set(0, 1, 1)

            # check for existing Sparse matrix is empty
            self.assertEqual(self.sparse_matrix.add_movie(newTestSparseMatrixObj), "sparse matrix is empty, please insert the values in sparse matrix")

            # set the sparse matrix
            self.sparse_matrix.set(0, 0, 1)
            self.sparse_matrix.set(0, 1, 2)
            self.sparse_matrix.set(1, 1, 3)
            self.sparse_matrix.set(1, 2, 4)

            # Check for row and column size matches the existing Sparse matrix
            self.assertEqual(self.sparse_matrix.add_movie(newTestSparseMatrixObj), "row and col size must match with existing matrix")

            newSparseMatrixObj = sparse_recommender.SparseMatrix(2,3)
            # set the new sparse matrix
            newSparseMatrixObj.set(0, 0, 1)
            newSparseMatrixObj.set(0, 2, 2)
            newSparseMatrixObj.set(1, 0, 3)
            newSparseMatrixObj.set(1, 1, 4)

            # test for addition two Sparse Matrices
            self.assertEqual(self.sparse_matrix.add_movie(newSparseMatrixObj).matrixdata,{(0, 0): 2, (0, 1): 2, (0, 2): 2, (1, 0): 3, (1, 1): 7, (1, 2): 4})

        except Exception as e:
            print(str(e))


    def test_to_dense_matrix(self):
        try:

            # check for elements in new Sparse Matrix
            self.assertEqual(self.sparse_matrix.to_dense(), "sparse matrix is empty, please insert the values in sparse matrix")

            # set the sparse matrix
            self.sparse_matrix.set(0, 0, 1)
            self.sparse_matrix.set(0, 1, 2)


            # check for Dense Matrix conversion
            self.assertEqual(self.sparse_matrix.to_dense(), {(0, 0): 1, (0, 1): 2, (0, 2): 0, (1, 0): 0, (1, 1): 0, (1, 2): 0})

            self.sparse_matrix.set(1, 2, 2)
            self.assertEqual(self.sparse_matrix.to_dense(), {(0, 0): 1, (0, 1): 2, (0, 2): 0, (1, 0): 0, (1, 1): 0, (1, 2): 2})



        except Exception as e:
            print(str(e))
