def solution(dic):
    l = dic.values()
    max_val = max(l)
    min_val = min(l)
    return (max_val,min_val)


dic = {'a': 1, 'b': 2, 'c': 3}
print solution(dic)
