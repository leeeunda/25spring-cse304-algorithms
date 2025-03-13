# name: 이다은
# student id: 2020100684
def fib2(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    f = [0] * (n + 1)
    f[0], f[1] = 0, 1  

    for i in range(2, n + 1):
        f[i] = f[i - 1] + f[i - 2]
    return f[n]