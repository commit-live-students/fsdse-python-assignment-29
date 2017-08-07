def solution(dic):
    max_value = max([v for k,v in dic.iteritems()])
    min_value = min([v for k,v in dic.iteritems()])
    return (max_value, min_value)
