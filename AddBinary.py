def solution(a,b):
    ans = ""
    i = len(a) - 1
    j = len(b) - 1
    carry = 0

    while i >= 0 or j >= 0 or carry:
        ones = 0
        if i >= 0 and a[i] == '1':
            ones += 1 
        if j >= 0 and b[j] == '1':
            ones += 1 
        if carry == 1:
            ones += 1 
        
        if ones == 0:
            ans = ans + "0"
        elif ones == 1:
            ans = ans + '1'
            carry = 0
        elif ones == 2:
            ans = ans + '0'
            carry = 1
        else:
            ans = ans + '1'
            carry = 1

        i -= 1 
        j -= 1 
    return ans[::-1]
print(solution("0", "0"))