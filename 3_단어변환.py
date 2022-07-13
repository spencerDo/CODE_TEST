from collections import deque

def check(s, start):
    answer = 0
    for i in range(len(s)):
        if list(s)[i] != list(start)[i]:
            answer += 1
    return True if answer == 1 else False


def solution(start, target, words):
    if target not in words:
        return 0

    queue = deque()
    queue.append([start, []])

    while queue:
        n, l = queue.popleft()
        for word in words:
            if word not in l and check(word, n):
                if word == target:
                    return len(l) + 1
                target = l[0:]
                target.append(word)
                queue.append([word, target])

    return 0
