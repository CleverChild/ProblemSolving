def solution(prices):
    
    answer =  [i for i in range(len(prices))]
    answer.reverse()
    for i in range (0, len(prices)):
        for j in range (i+1, len(prices)):
            if prices[i] > prices[j]:
                answer[i]=j-i
                break

    return answer