def solution(dic):
    for key in dic:
        key_max = max(dic.keys(), key=(lambda k: dic[k]))
        key_min = min(dic.keys(), key=(lambda k: dic[k]))

        return(dic[key_max],dic[key_min])
#        return(dic[key_min])

print solution({'x':500, 'y':5874, 'z': 560})
