size = int(input())
num =list(map(int,input().split()))
crimes,officers = 0,0
for i in range(size):
    if num[i] != -1 :
        officers +=num[i]
    elif num[i] == -1 :
        if officers > 0:
            officers-=1
        else:
            crimes+=1
    
    
print(crimes)
