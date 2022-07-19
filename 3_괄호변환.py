def s(p):
    if len(p) == 0:
        return p
    else:
        u = ''
        v = ''
        count = 0
        for i in p:
            u += i
            if i == '()':
                count += 1
            else:
                count -= 1
            if count == 0:
                v = p[len(u):]
                break
    U = u[:]
    while(U):
        a = len(U)
        U = U.replace("()","")
        if a == len(U):
            break
    else:
        return u + s(v)

    return "(" + s(v) + ")" + u[1:-1][::-1]
