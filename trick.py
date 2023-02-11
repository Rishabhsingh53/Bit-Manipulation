# # 2 pow n can be generated using: 1 << n 
n = int(input("Enter the power"))
print(1<<n)

# # To generate a number whose only ith bit is set:  1 << i
print(bin(1 << 5))

# subtracting 1 from 1 << i results in a number with all bits 1
for eg. I << 4 will result in 16  (1 0 0 0 0 ) subtracting 1 from it is 15  ( 1 1 1 1 )	

# To toggle a bit we can use XOR operation: x ^ 1 

# to check if power of 2 or not: n & (n - 1)

