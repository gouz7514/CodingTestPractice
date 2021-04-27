N = int(input()) # 모험가 수
scare = list(map(int, input().split(' '))) # 공포도
result = []
answer = 0
scare.sort(reverse = True) # 내림차순 정렬
print(scare)

group = []
tmp = 0
for i in range(len(scare)):
    if tmp == 0:
        tmp = scare[i]
    if tmp != 0:
        if len(group) < tmp:
            group.append(scare[i])
        if len(group) == tmp:
            result.append(group)
            answer += 1
            group = []
            tmp = 0

print(result)
print(answer)