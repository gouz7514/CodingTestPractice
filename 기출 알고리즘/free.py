sentence = 'i love coding'
keyword = 'mask'
skips = [0, 0, 3, 2, 3, 4]


def solution(sentence, keyword, skips):
    sentence_reverse = list(sentence)[::-1]
    answer = []
    for i in range(len(skips)):
        key = keyword[i % len(keyword)]
        if skips[i] == 0:
            answer.append(key)
        else:
            while skips[i] > 0:
                s = sentence_reverse.pop()
                answer.append(s)
                if s == key:
                    answer.append(key)
                    break
                skips[i] -= 1
            answer.append(key)

    answer += sentence_reverse[::-1]
    return ''.join(answer)


print(solution(sentence, keyword, skips))
