# 잃어버린 괄호
# 문제 링크 : https://www.acmicpc.net/problem/1541
# 문제 이해 : 2분 20초
# 문제 해결 : 50분 초과
# 이 쉬운 거를 난 왜 이렇게 어렵게 풀었지????
# 그래도 -를 기준으로 다 더하고 뺀다는 개념은 파악함
# s = input()
# t = []
# operator = ['+','-']
# x = ''
#
# for i in s:
#     if i.isnumeric():
#         x += i
#     elif i in operator:
#         t.append(int(x))
#         t.append(i)
#         x = ''
# t.append(int(x))
# print("t : ", t)
# result = t[0]
# right = 0
# minus_flag = False
#
# for i in range(1, len(t)-1):
#     if t[i] == '-':
#         minus_flag != minus_flag
#         result -= right
#         right = 0
#     elif t[i] == '+':
#         if minus_flag:
#             right += t[i+1]
#         else:
#             result += t[i+1]
#
# print(result)

a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)