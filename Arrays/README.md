# Problem Name:  Set Matrix Zeroes 
# Link: [click me](https://www.codingninjas.com/codestudio/problems/set-matrix-zeros_3846774)

# Approach (Using two extra arrays): #

The steps are as follows:

1.  First, we will declare two arrays: a row array of size N and a col array of size M and both are initialized with 0.
2.  Then, we will use two loops(nested loops) to traverse all the cells of the matrix.
3.  If any cell (i,j) contains the value 0, we will mark ith index of row array i.e. row[i] and jth index of col array col[j] as 1. It signifies that all the elements in the ith row and jth column will be 0 in the final matrix.
4.  We will perform step 3 for every cell containing 0.
5.  Finally, we will again traverse the entire matrix and we will put 0 into all the cells (i, j) for which either row[i] or col[j] is marked as 1.
6.  Thus we will get our final matrix.

# Complexity Analysis #

__Time Complexity__: O(2*(N*M)), where N = no. of rows in the matrix and M = no. of columns in the matrix.

Reason: We are traversing the entire matrix 2 times and each traversal is taking O(N*M) time complexity.

__Space Complexity__: O(N) + O(M), where N = no. of rows in the matrix and M = no. of columns in the matrix.

Reason: O(N) is for using the row array and O(M) is for using the col array.
