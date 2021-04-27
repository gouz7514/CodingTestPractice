n, m = map(int, input().split()) # 4, 2
check = [True] * n
arr = []

def sol(k):
    if k == m:
        print(*arr)
        return
    for i in range(k, n):
        if check[i]:
            check[i] = False
            arr.append(i+1)
            sol(k+1)
            arr.pop()

            # 아래 부분이 순열과의 차이점
            # 전에 봤던 것을 닫아준다?
            for j in range(i+1, n):
                check[j] = True
sol(0)