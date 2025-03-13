# name: 이다은
# student id: 2020100684
from typing import List

def matrixmult(n: int, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
    C = [[0] * n for _ in range(n)]
    for i in range(n):  
        for j in range(n):  
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    return C