# 폴리오미노
# 문제 링크 : https://www.acmicpc.net/problem/1343
# 문제 이해 : 1분 45초
# 문제 해결 : 17분 23초
# 잘 푼거같은데 코드가 이렇게 길 필요가 있을까?
# 문자열 바꾸기인데 왜 이렇게 어렵게 생각했지??
# board = list(input())
# start = 0
# answer = []
# flag = True
#
# while start != len(board):
#     if board[start] == '.':
#         answer.append('.')
#         start += 1
#     else:
#         if start + 4 <= len(board) and board[start:start+4] == ['X'] * 4:
#             answer.extend(['A'] * 4)
#             start += 4
#         elif start + 2 <= len(board) and board[start:start+2] == ['X'] * 2:
#             answer.extend(['B'] * 2)
#             start += 2
#         else:
#             flag = False
#             break
#
# if flag:
#     print(''.join(answer))
# else:
#     print(-1)

board = input()
board = board.replace('XXXX','AAAA')
board = board.replace('XX', 'BB')

if 'X' in board:
    print(-1)
else:
    print(board)