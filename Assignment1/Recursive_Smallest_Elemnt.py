#2.1 (a) Give a recursive (decrease-by-one) algorithm for finding the position of 
#the smallest element in an array of n real numbers.

def smallest(a,small,idx,small_idx):
  #print(a[0])
  n = len(a)
  #print(n)
  if n == 0:
    return (small_idx)
  else:
    
    if a[0] < small:
      small = a[0]
      small_idx = idx
      idx = idx+1
      return smallest(a[1:], small,idx,small_idx)
    else:
      idx = idx+1
      return smallest(a[1:], small,idx,small_idx)
      
      f = smallest([4,3,1,3,-7,-1,-10],4,0,0)
