# 뒤집기
# 문제 링크 : https://www.acmicpc.net/problem/1439
# 문제 이해 : 1분 30초
# 문제 해결 : 20분 22초
# 개수로 접근했다가 아닌 것을 깨닫고 인덱스로 접근해서 풀이함.
# 연속된 인덱스가 나타나는 횟수를 세서 마지막에 비교

# 와 씨바 잘 풀었다고 생각하는데 다른 사람들 개 쩌네
# 내 풀이
# S = list(input())
# zero = []
# one = []
# answer = 0
#
# for i in range(len(S)):
#     if S[i] == '0':
#         zero.append(i)
#     else:
#         one.append(i)
#
# # zero의 경우
# z_answer = 0
# if len(zero):
#     start_z = zero[0]
#     for i in range(1, len(zero)):
#         if zero[i] != start_z + 1:
#             z_answer += 1
#         start_z = zero[i]
#
#     z_answer += 1
#
# # one의 경우
# o_answer = 0
# if len(one):
#     start_o = one[0]
#     for i in range(1, len(one)):
#         if one[i] != start_o + 1:
#             o_answer += 1
#         start_o = one[i]
#     o_answer += 1
#
# answer = z_answer if z_answer < o_answer else o_answer
# print(answer)

# 남의 풀이
# 바뀌는 횟수만 체크한다.
S = input()
count = 0
for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1
print((count + 1) // 2)