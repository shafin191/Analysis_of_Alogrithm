#2.4. An array A[1 . . n] of integers is a mountain if it consists of an increasing sequence
#followed by a decreasing sequence, or more precisely,If there is an index m ∈ {1, 2, . . . , n} such that
#• A[i] < A[i + 1] for all 1 ≤ i < m, and
#• A[i] > A[i + 1] for all m ≤ i < n.
#In particular, A[m] is the maximum element, and it is the unique “locally maximum” element
#surrounded by smaller elements (A[m − 1] and A[m + 1]).
#Give an algorithm to compute the maximum element of a mountain input array A[1 . . n] in
#O(log(n)) time.


import math
def max_in_mountain(A):
  n = len(A)-1
  l= 1
  r = n
  while l<=r:
    mid = math.floor((l+r)/2)
    if mid ==1:
      return 'None'
    else:
      left = mid-1

    if mid == n:
      return 'None'
    else:
      right = mid+1

    if (A[mid] > A[left]) and (A[mid] > A[right]):#Need some modification here
      return A[mid]
    else:
      if (A[mid] > A[left]) and (A[mid] < A[right]):#Need some modification here
        l = mid +1
      elif (A[mid] < A[left]) and (A[mid] > A[right]):#Need some modification here
        r = mid-1
  
  return 'None'
  
  print(['None',1,2,3,4,5,6,11,7,13])
