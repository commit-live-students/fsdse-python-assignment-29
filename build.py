def solution(dic):
    maxvalue = max(dic.iterkeys(), key=lambda k: dic[k])
    minvalue = min(dic.iterkeys(), key=lambda k: dic[k])
    return (dic[maxvalue],dic[minvalue])



dict_available = {'a': 1, 'b': 2, 'c': 3}
solution(dict_available)
