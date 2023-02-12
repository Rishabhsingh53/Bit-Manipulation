def minBitFlips(start: int, goal: int) -> int:
    ans = 0
    for i in range(32):
        val1 = start & (1 << i) 
        val2 = goal  & (1 << i)

        if val1 ^ val2 :
            ans += 1 

    return ans

print(minBitFlips(10,7))