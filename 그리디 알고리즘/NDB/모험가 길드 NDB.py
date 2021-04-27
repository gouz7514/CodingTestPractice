n = int(input())
scare = list(map(int, input().split()))
scare.sort()

result = 0 # 총 그룹의 수
cnt = 0 # 현재 그룹에 포함된 모험가의 수

for i in scare:
    cnt += 1
    if cnt >= i:
        result += 1
        cnt = 0

print(result)