# 이름: 이다은
# 학번: 2020100684

from typing import List

def seqsearch(n: int, S: List[int], x: int) -> int: 
    for i in range(n):
        if S[i]==x:
            return i
    return -1