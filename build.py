def solution(dic):
    max_value = max(dic.iterkeys(), key=lambda k: dic[k])
    #return max_value
    min_value = min(dic.iterkeys(), key=lambda k: dic[k])
    #return min_value
    return (dic[max_value],dic[min_value])



dict_available = {'a': 1, 'b': 2, 'c': 3}
solution(dict_available)
