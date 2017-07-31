def solution(dic):
    s=sorted(dic.values())
    print(s)
    return (s[-1],s[0])
print(solution({'x': 500, 'y': 5874, 'z': 560}))
