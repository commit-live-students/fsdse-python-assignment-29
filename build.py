def solution(dic):
    "Enter Code here"
    i = 0
    vec = []
    output = ()

    while i < len(dic):
        k, v = dic.items()[i]
        vec.append(v)
        i = i + 1

    maximum = max(vec)
    minimum = min(vec)
    output = (maximum, minimum)
    return output


'''
a = {1: 12, 2: 24, 3: 36, 4: 1}
b = solution(a)
print b
'''
