import numpy as np

class Matrix:
    """
        Note: I have named all these functions some variation
            of multiply, but the multiplication operation is only
            tested for square matrices.

            I might modify these later to take matrices of any dimensions
            but at present they are not tested to handle that.
    """
    @staticmethod
    def multiply(a, b):
        # dimensions of a is m x n
        # dimensions of b is n x p
        if len(a[0]) != len(b):
            raise Exception("Multiplication not supported for given Inputs")
        
        c = np.zeros((len(a), len(b[0])))

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    c[i][j] += a[i][k] * b[k][j]

        return c
    
    @staticmethod
    def recursive_mul(a:np.ndarray, b:np.ndarray):
        if a.shape == (2, 2) and b.shape == (2, 2):
            return Matrix.multiply(a, b)
        
        ...

    @staticmethod
    def strassens(a, b):
        ...