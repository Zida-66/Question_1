def solution(m, n, sum):
    answer = ""
    i = j = k = l = 0
    tmp = (n - 1)+(m + 1) * m/2
    dif = sum - tmp
    down = dif / (n-1)
    right = dif % (n-1)
    
    while i < down-1:
        answer += "D"
        i += 1
        
    while j < n-right-1:
        answer += "R"
        j += 1

    answer += "D"

    while k < right:
        answer += "R"
        k += 1

    while l < m-down-2:
        answer += "D"
        l += 1

    return answer


A = solution(9,9,65)
B = solution(9,9,72)
C = solution(9,9,90)
D = solution(9,9,110)

E = solution(90000,100000,87127231192)
F = solution(90000,100000,5994891682)

f = open("output_question_1.txt","w")
f.write(str("65 "+ A + "\n"))
f.write(str("72 " + B + "\n"))
f.write(str("90 " + C + "\n"))
f.write(str("110 " + D + "\n"))
f.write(str("87127231192 " + E + "\n"))
f.write(str("5994891682 " + F + "\n"))


