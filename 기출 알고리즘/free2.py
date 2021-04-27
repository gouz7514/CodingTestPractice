import sys

for _ in range(int(sys.stdin.readline())):
    n, m = map(int, sys.stdin.readline().split())
    cnt = 0
    for a in range(1, n-1):
        for b in range(a+1, n):
            x = (a**2 + b**2 + m) / (a * b)
            if x == int(x):
                cnt += 1
    print(cnt)
