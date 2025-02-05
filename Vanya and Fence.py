num,hig =map(int,input().split())
n=list(map(int,input().split()))
sum=0
for i in range(num):
    if n[i] <= hig:
        sum +=1
    else:
        sum +=2
print(sum)
