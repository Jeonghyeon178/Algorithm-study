def solution(sizes):
    
    for i in sizes:
        i.sort()
    
    max_x = 0
    max_y = 0
    for x, y in sizes:
        if max_x < x:
            max_x = x
        if max_y < y:
            max_y = y
    
    return max_x * max_y