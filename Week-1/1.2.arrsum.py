# 이름: 이다은
# 학번: 2020100684

from typing import List

def arrsum(n: int, S: List[int]) -> int:
    # Complete the code here
    total=0
    if len(S)==0:
        return 0
    for i in range(n):
        total+=S[i]
    return total