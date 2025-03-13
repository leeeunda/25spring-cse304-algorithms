# name: 이다은
# student id: 2020100684
from typing import List

def binsearch(n: int, S: List[int], x: int) -> int:
    low, high = 0, n - 1
    location = -1
    for _ in range(n):
        mid=(low+high)//2
        if low>high:
            break
        if S[mid]==x:
            return mid
        elif S[mid]<x:
            low=mid+1
        else:
            high=mid-1
    return location