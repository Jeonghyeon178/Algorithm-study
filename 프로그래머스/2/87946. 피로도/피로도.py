from itertools import permutations

def solution(k, dungeons):
    cnt = 0
    
    for i in permutations(dungeons):
        tmp_k = k
        tmp_cnt = 0
        
        for i1, i2 in i:
            if tmp_k >= i1:
                tmp_k -= i2
                tmp_cnt += 1
            else:
                break
        
        cnt = max(tmp_cnt, cnt)
        
    
    return cnt