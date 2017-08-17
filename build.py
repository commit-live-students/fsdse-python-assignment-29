def solution(dic):

    m = max(dic.values())
    n = min(dic.values())
    t = (m,n)
    return t
print solution({'a': 1, 'b': 2, 'c': 3})
