# 박 터뜨리기
# 문제 링크 : https://www.acmicpc.net/problem/19939
# 문제 이해 : 2분 5초
# 문제 해결 : 20분 초과
# 와 이걸 이렇게 풀 수 있구나
# 최소한의 경우는 당연히 등차수열, 그러니까 1 ~ K까지 합이 N보다 크면 불가능함
# 아닌 경우 가장 많이 담긴 바구니부터 1개씩 차례대로 할당
# 여분의 공이 K의 배수인 경우 K - 1
# 아닌 경우 가장 많이 담긴 바구니는 추가로 하나 더 할당. 따라서, K
N, K = map(int, input().split())


def check(n, k):
    if n < k * (k + 1) // 2:
        return -1
    else:
        left = n - k * (k + 1) // 2
        if left % k == 0:
            return k - 1
        else:
            return k


print(check(N, K))
