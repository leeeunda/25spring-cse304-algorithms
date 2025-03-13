from typing import List

def exchangesort(n: int, S: List[int]) -> None:
    # Complete the code here
    for i in range(n-1):
        for j in range(i+1, n): #i아님. i보다 뒤에 있는 원소
            if S[i]>S[j]:
                S[i],S[j]=S[j],S[i]