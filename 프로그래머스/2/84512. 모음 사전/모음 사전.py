def solution(word):
    answer = 0
    
    li = [781, 156, 31, 6, 1]
    
    for i in range(len(word)):
        if word[i] == "A":
            answer += li[i] * 0 + 1
        elif word[i] == "E":
            answer += li[i] * 1 + 1
        elif word[i] == "I":
            answer += li[i] * 2 + 1
        elif word[i] == "O":
            answer += li[i] * 3 + 1
        elif word[i] == "U":
            answer += li[i] * 4 + 1
        else:
            print("wtf")
    return answer