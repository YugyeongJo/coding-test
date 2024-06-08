import sys

N = int(input())
input = sys.stdin.readline

for add in range(N):
    a,b = map(int, input().rstrip().split())
    result = a + b
    print(result)