def solution(begin, target, words):
    distance = [0 for i in words]  # 거리 나타낼 배열
    if target not in words:
        return 0

    def dfs(begin, target, words, distance):
        stack = [begin]
        while 0 in distance:
            x = stack.pop()
            max_dist = max(distance)
            for word in words:
                diff = 0
                for a, b in zip(x, word):
                    if a != b:
                        diff += 1
                # 한글자만 다르고 아직 방문하지 않았으면
                if diff == 1 and distance[words.index(word)] == 0:
                    distance[words.index(word)] = max_dist + 1
            if x == target: # 종료 조건
                return distance
            stack.append(words[distance.index(max(distance))])
        return distance

    answer = dfs(begin, target, words, distance)
    return answer[words.index(target)]