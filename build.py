def solution(dic):
    max_value = 0
    min_value = 0
    list1 = sorted(dict1.iteritems())
    max_value = max(list1, key=lambda list1:list1[1])
    min_value = min(list1, key=lambda list1:list1[1])
    #print max_value
    #print min_value
    tuple_numbers = max_value[1], min_value[1]
    return tuple_numbers

dict1 = {'x': 500, 'y': 5874, 'z': 560}
solution(dict1)
