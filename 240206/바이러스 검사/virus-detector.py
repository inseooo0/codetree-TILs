import sys
import math
input = sys.stdin.readline

n = int(input())
customers = list(map(int, input().split()))
n1, n2 = map(int, input().split())

cnt = n

for c in customers:
    p = 0
    p += n1
    if p < c:
        cnt += math.ceil((c - n1) / n2)

print(cnt)