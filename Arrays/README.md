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



# Problem Name:  Reverse Pairs 
# Link: [click me](https://www.codingninjas.com/codestudio/problems/reverse-pairs_1112652)

# Intuition: #

We will be using the Merge Sort Algorithm to solve this problem. We split the whole array into 2  parts creating a Merge Sort Tree-like structure. During the conquer step we do the following task : 

    a.  We take the left half of the Array and Right half of the Array, both are sorted in themselves.
    b.  We will be checking the following condition arr[i] <= 2*arr[j]  where i is the pointer in the Left Array and j is the pointer in the Right Array.
    c.  If at any point arr[i] <= 2*arr[j] , we add 1  to the answer as this pair has a contribution to the answer. 
    d.  If Left Array gets exhausted before Right Array we keep on adding the distance j pointer traveled as both the arrays are Sorted so the next ith element from Left Subarray will equally contribute to the answer.

The moment when both Arrays get exhausted we perform a merge operation. This goes on until we get the original array as a Sorted array.

# Approach: #

The steps are as follows:

1.  We, first of all, call a Merge Sort function, in that we recursively call Left Recursion and Right Recursion after that we call the Merge function in order to merge both Left and Right Calls we initially made and compute the final answer.
2.  In the Merge function, we will be using low, mid, and high values to count the total number of inversion pairs for the Left half and Right half of the Array.
3.  Now, after the above task, we need to Merge the both Left and Right sub-arrays using a temporary vector.
4.  After this, we need to copy back the temporary vector to the Original Array. Then finally we return the number of pairs we counted.

# Complexity Analysis #

__Time Complexity__: O( N log N ) + O (N) + O (N)   

Reason: O(N) – Merge operation, O(N) – counting operation ( at each iteration of i, j doesn’t start from 0 . Both of them move linearly ) 

__Space Complexity__: O(N) 

Reason : O(N) – Temporary vector
