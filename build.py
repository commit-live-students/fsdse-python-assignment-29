def solution(dic):
    "Enter Code here"
    values = sorted(dic.values())
    result = [values[len(values)-1], values[0]]
    return tuple(result)
