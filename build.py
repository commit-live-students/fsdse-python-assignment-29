def solution(dic):
    "Enter Code here"
    d1 = sorted(dic.values())
    return d1[-1], d1[0]

d = {'a': 1, 'b': 2, 'c': 3}
print(solution(d))
