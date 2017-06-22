def solution(dic):
    "Enter Code here"
    import numpy as np
    arr = np.asarray(dic.values())
    return (arr.max(),arr.min())
