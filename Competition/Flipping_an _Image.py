# Flipping an Image
# Given a binary matrix A, we want to flip the image horizontally,
# then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  
# For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. 
# For example, inverting [0, 1, 1] results in [1, 0, 0]

class Solution:
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        for i in range(len(A)):  
            A[i] = A[i][::-1]  
        for i in range(len(A)):
            for j in range(len(A[i])):
                if A[i][j] == 0:
                    A[i][j] = 1
                else:
                    A[i][j] = 0
        return A