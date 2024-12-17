from itertools import permutations

def solution(numbers):
    answer = 0
    set_numbers = set()
    
    for i in range(1, len(numbers) + 1):
        p = permutations(numbers, i)
        for j in p:
            num = int("".join(j))
            set_numbers.add(num)
    
    print(set_numbers)
    
    for i in set_numbers:
        if i < 2:
            continue
        tf = True
        for j in range(2, int(i**0.5) + 1):
            if i % j == 0:
                tf = False
                break
        if tf:
            answer += 1
    
    return answer