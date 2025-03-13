# name: 이다은
# student id: 2020100684
def fib1(n: int) -> int:
    # Complete the code here
    if n==1:
        return 1
    elif n==0:
        return 0
    return fib1(n-1)+fib1(n-2)