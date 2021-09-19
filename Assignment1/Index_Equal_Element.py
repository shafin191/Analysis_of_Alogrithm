#2.3. Given a sorted array A of n distinct integers, some of which may be negative, give an
#O(log(n)) algorithm to find an index i such that 1 ≤ i ≤ n and A[i] = i provided such an index
#exists. If there are many such indices, the algorithm can return any one of them

import math

def index_equal_element(A,start,end):
    if end >= start:
        mid = math.floor((start+end)/2)
        
        if A[mid] == mid:
            return mid
        elif mid < A[mid]:
                return index_equal_element(A,start,mid-1)
        elif mid > A[mid]:
                return index_equal_element(A,mid+1,end)       
    else:
        return -1

def find_sol(A):
  n= len(A)
  ans = index_equal_element(A,1,n-1)
  if ans == -1:
    print('No solution found')
  else:
    print("Solution found at: " + str(ans))
  
  
#Function Calling
find_sol(['None',-6,-4,-2, 3, 4,5,7,10,12])
