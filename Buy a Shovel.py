k,r= map(int, input().split())
temp = k
count = 1
while k%10 != 0 and k%10 != r:
    k += temp
    count += 1
print(count)
