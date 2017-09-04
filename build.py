def solution(dic):
    d1=dic.values()
    d1.sort()
    return (d1[-1],d1[0])

print solution({10:50,2:30,1:50,4:60,3:20,6:80})
