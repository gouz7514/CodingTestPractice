# 전구와 스위치
# 문제 링크 : https://www.acmicpc.net/problem/2138
# 문제 이해 : 50초
# 문제 해결 : 30분 초과
# 아래 방식은 완전히 틀림(범위나누는 방식)

# 1. 첫번째 스위치를 누르는 / 누르지 않는 경우
# 2. 한번 지나간 전구는 다시 건드리지 않음
# 3. 두번째 전구부터 시작해서 이전 전구의 상태가 희망하는 상태와 같은지 확인하고 다르면 스위치 눌러 상태 변경
#########
# def zeroClick(state):
#     count=1
#     state[0]=int(not state[0])
#     state[1] = int(not state[1])
#     for i in range(1,n):
#         if(state[i-1]!=result[i-1]):
#             count+=1
#             state[i-1]=int(not state[i-1])
#             state[i]=int(not state[i])
#             if(i!=n-1):
#                 state[i+1]=int(not state[i+1])
#     if(state==result):
#         return count
#     else:
#         return -1
# def zeroNoClick(state):
#     count=0
#     for i in range(1,n):
#         if(state[i-1]!=result[i-1]):
#             count+=1
#             state[i-1]=int(not state[i-1])
#             state[i]=int(not state[i])
#             if(i!=n-1):
#                 state[i+1]=int(not state[i+1])
#     if(state==result):
#         return count
#     else:
#         return -1
#
# n = int(input())
# state = list(input())
# result = list(input())
# res1 = zeroClick(state[:])
# res2 = zeroNoClick(state[:])
# if(res1>=0 and res2>=0):
#     print(min(res1,res2))
# elif(res1>=0 and res2<0):
#     print(res1)
# elif(res1<0 and res2>=0):
#     print(res2)
# else:
#     print(-1)
##########

N = int(input())
now = list(map(int, input()))
target = list(map(int, input()))


def change(n):
    return (n+1) % 2

def set_pair(now, count):
    if count:
        now[:2] = [change(now[0]), change(now[1])]

    for i in range(1, N):
        if now[i-1] != target[i-1]:
            count += 1
            now[i-1] = change(now[i-1])
            now[i] = change(now[i])
            if i < N-1:
                now[i+1] = change(now[i+1])
    return count if now == target else -1

res1 = set_pair(now[:], 0)
res2 = set_pair(now[:], 1)

if res1 >= 0 and  res2 >= 0:
    print(min(res1, res2))
elif res1 >= 0 and res2 < 0:
    print(res1)
elif res1 < 0 and res2 >= 0:
    print(res2)
else:
    print(-1)
