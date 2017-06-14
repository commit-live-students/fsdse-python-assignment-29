def solution(dic):
    maxi=max(dic.values())
    mini=min(dic.values())
    l=[]
    l.append(maxi)
    l.append(mini)
    return tuple(l)

print(solution({'a': 1, 'b': 2, 'c': 3}))
