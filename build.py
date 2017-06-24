def solution(dic):
    key_max = max(dic.keys(), key=(lambda k: dic[k]))
    key_min = min(dic.keys(), key=(lambda k: dic[k]))

    val = (dic[key_max] , dic[key_min])
    return val

print solution({'a': 1, 'b': 2, 'c': 3})
