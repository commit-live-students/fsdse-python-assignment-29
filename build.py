a = {'a': 1, 'b': 2, 'c': 3}

def solution(dic):
    val = dic.values()
    val.sort()
    tup = (val[-1], val[0])
    return tup

solution(a)
