# def dfs(start, depth):
#     if depth == 6:
#         for i in range(6):
#             print(combi[i], end=' ')
#         print()
#         return
#     for i in range(start, len(s)):
#         combi[depth] = s[i]
#         dfs(i + 1, depth + 1)
#
# combi = [0 for i in range(13)]
#
# while True:
#     s = list(map(int, input().split()))
#     if s[0] == 0:
#         break
#     del s[0]
#     dfs(0, 0)
#     print()
####
def lotto(x, cnt):
    if cnt == 6:
        for i in range(k):
            if select[i]:
                print(a[i], end=' ')
        print()
        return

    for i in range(x, k):
        select[i] = 1
        lotto(i+1, cnt+1)
        select[i] = 0

while True:
    a = list((map(int, input().split())))
    k = a[0]
    if k == 0:
        break
    a = a[1:]
    select = [0 for _ in range(k)]
    lotto(0, 0)
    print()