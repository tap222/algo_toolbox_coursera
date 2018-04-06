# Uses python3
def cal_fib_efficient(n):
    if n <= 1:
        return n
    previous, current = 0,1
    for i in range(2,n+1):
        new = previous + current
        previous = current
        current  = new 
    return new

n = int(input())

print(cal_fib_efficient(n))
