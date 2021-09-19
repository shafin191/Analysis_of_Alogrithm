#Given a real number x and given a sequence of real numbers a0, a1, a2, …, an-1. Give an
#algorithm to find the value of the ∑𝑛 𝑖=−01 𝑎𝑖 𝑥𝑖. Analyze the complexity of your solution. For
#full grade you need to give a O(n) algorithm. Please note that the basic operations are:
#addition/subtraction, multiplication/division, memory access, and read/write operations. In
#particular, i multiplications need i basic steps

def find_eq_val(A,x):
  sum = A[0]
  for i in range(1,len(A)):
    sum = sum + A[i] * x
    x = x*x
  return sum
  
ans=find_eq_val([2,3,7,11],5)
print(ans)
