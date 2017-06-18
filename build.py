my_dict = {'a': 1, 'b': 2, 'c': 3}
list1=[]
def solution(my_dict):
    key_min = min(my_dict.keys(), key=(lambda k: my_dict[k]))
    key_max = max(my_dict.keys(), key=(lambda k: my_dict[k]))

    list1=(my_dict[key_max],my_dict[key_min])
    return tuple(list1)
solution(my_dict)
