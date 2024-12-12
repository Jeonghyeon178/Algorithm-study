def solution(answers):
    answer = []

    pattern_1 = [1, 2, 3, 4, 5]
    pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    case_1 = pattern_1 * (len(answers) // len(pattern_1)) + pattern_1[:len(answers) % len(pattern_1)]
    case_2 = pattern_2 * (len(answers) // len(pattern_2)) + pattern_2[:len(answers) % len(pattern_2)]
    case_3 = pattern_3 * (len(answers) // len(pattern_3)) + pattern_3[:len(answers) % len(pattern_3)]
    cnt = [0, 0, 0, 0]
    
    for i in range(len(answers)):
        if case_1[i] == answers[i]:
            cnt[1] += 1
        if case_2[i] == answers[i]:
            cnt[2] += 1
        if case_3[i] == answers[i]:
            cnt[3] += 1
    
    tmp = max(cnt)
    for i in range(len(cnt)):
        if tmp == cnt[i]:
            answer.append(i)
    
    return answer