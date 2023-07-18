class MainDiagonal():
    def sum(self, u_input):
        row = u_input[0]
        sum = 0
        a = 2
        for i in range(row):
            new_array = u_input[a: row+a]
            sum += new_array[i]
            a+=row

        return sum

u_input = list(map(int, input().split()))
object = MainDiagonal()
print(object.sum(u_input))

"""You are given a N X N integer matrix. You have to find the sum of all the main diagonal elements of A.
Main diagonal of a matrix A is a collection of elements A[i, j] such that i = j.

Input Format
There are 1 lines in the input. First 2 integers R, C are the number of rows and columns. 
Then R * C integers follow corresponding to the row-wise numbers in the 2D array A.

Output Format
Return an integer denoting the sum of main diagonal elements."""