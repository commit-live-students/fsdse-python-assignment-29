def solution(dic):
    "Enter Code here"
    l = []
    for x in dic.values():
        l.append(x)
    a = max(l)
    b = min(l)
    c = (a,b)
    return c
