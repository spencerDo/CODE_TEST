def solution(p):
    if len(p) == 0:
        return p
    else:
        u = ''
        v = ''
        count = 0
        for i in p:
            u += i
            if i == '(':
                count += 1
            else:
                count -= 1
            if count == 0:
                v = p[len(u):]
                break
    result = u[:]
    while(result):
        a = len(result)
        result = result.replace("()","")
        if a == len(result):
            break
    else:
        return u + solution(v)

    return "(" + solution(v) + ")" + u[1:-1][::-1]
