#3..3(a) Given an array of positive and negative integers, write the main ideas of an algorithm to
#segregate them without changing the relative order of elements. The output should contain
#all positive numbers follow negative numbers while maintaining the same relative ordering.
#Example:
#Input: [9, -3, 5, -2, -8, -6, 1, 3]
#Output: [-3, -2, -8, -6, 9, 5, 1, 3]

def segregate_array(a,n):
  b = [None] * n
  idx = 0

  for i in a:
    if i < 0:
      b[idx] = i
      idx=idx+1
  
  for i in a:
    if i > 0:
      b[idx] = i
      idx=idx+1
    
  return b



inp= [9, -3, 5, -2, -8, -6, 1, 3]
segregate_array(inp,len(inp))
