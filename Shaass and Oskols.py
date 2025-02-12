size_w = int(input())
num_b = list(map(int, input().split()))
shote = int(input())

for i in range(shote):
    shot_b = list(map(int, input().split()))
    a = shot_b[0] - 1  
    b = shot_b[1]

    if a >= 0 and a < size_w:  
        if a - 1 >= 0:  
            num_b[a - 1] += b - 1
        if a + 1 < size_w:  
            num_b[a + 1] += num_b[a] - b
        num_b[a] = 0 


for i in range(size_w):
    print(num_b[i])
