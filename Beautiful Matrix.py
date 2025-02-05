matrix = []
r,c = 0,0
for i in range(5):
    n = list(map(int,input().split()))
    matrix.append(n)
for i in range(5):
    if 1 in matrix[i]:
        for j in range(5):
            if matrix[i][j] == 1:
                r=i
                c=j
                break
if r == 0 or r == 4:
    if c==0 or c==4:
        print(4)
    elif c==1 or c==3:
        print(3)
    else:
        print(2)
elif r == 1 or r == 3:
    if c==0 or c==4:
        print(3)
    elif c==1 or c==3:
        print(2)
    else:
        print(1)
elif r==2:
    if c==0 or c==4:
        print(2)
    elif c==1 or c==3:
        print(1)
    else:
        print(0)       
