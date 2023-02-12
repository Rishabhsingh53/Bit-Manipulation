def reverseBits( n: int) -> int:
    print(n)
    
    ans = bin(n)
    zeroes = '0' * (32 - (len(ans) - 2)) 
    ans = zeroes + ans[2:]
    
    ans = list(ans)

    for i in range(16):
        ans[i] , ans[len(ans)-i-1] = ans[len(ans)-i-1] , ans[i]
    ans = "".join(ans)
    val = int(ans, base = 2)
    return val

print(reverseBits(7))