def solution(dic):
    #print max(dic.values())
    #print min(dic.values())
    maximum = max(dic.values())
    minimum = min(dic.values())
    return (maximum, minimum)
dic = {'x': 500, 'y': 100, 'z': 560}
solution(dic)
