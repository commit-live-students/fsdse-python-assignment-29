def solution(dic):
    ls = dic.values()
    max = ls[0]
    min = ls[0]
    for e in ls:
        if (e<min):
            min = e
        if (e>max):
            max = e
    #print("Max and min are",(max,min))
    return (max,min)

t = solution({'a': 1, 'b': 2, 'c': 3,'d':4,'e':0})
print("Result tuple is:",t)
