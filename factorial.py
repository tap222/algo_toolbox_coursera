// From http://mkweb.bcgsc.ca/circos/guide/tables/
 import sys

 def factorial(n):
  if n == 0:
    return n
  new,curr = 1 , 1
  for i in range(1,n+1):
    total = new * curr
    new = total
    curr = curr + 1
  return total

input = sys.stdin.read()
n = int(input)
print(factorial(n))
