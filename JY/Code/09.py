def solution(s):
    l = len(s)
    answer = l
    half = l // 2
    
    for i in range(1, half + 1):
        sentence = ""
        
        prev = s[0:i]
        count = 1
        
        for j in range(i, l, i):
            if prev == s[j:j+i]:
                count += 1
            else:
                if count == 1 :
                    sentence += prev
                else:
                    sentence += str(count) + prev
                prev = s[j:j+i]
                count = 1
        
        if count == 1 :
            sentence += prev
        else:
            sentence += str(count) + prev 
    
        answer = min(answer, len(sentence))
    return answer