def solution(dic):
    "Enter Code here"
    maxKey = max(dic, key=dic.get)
    minKey = min(dic, key=dic.get)
    return (dic[maxKey],dic[minKey])

solution({'a': 1, 'b': 2, 'c': 3})
