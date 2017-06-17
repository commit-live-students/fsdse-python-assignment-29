def solution(dic):
    max_Key = max(dic, key=dic.get)
    min_Key = min(dic, key=dic.get)
    print (dic[max_Key],dic[min_Key])
    return (dic[max_Key],dic[min_Key])

solution({'a': 1, 'b': 2, 'c': 3})
