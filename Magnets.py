size = int(input())
pole=[]
for i in range(size):
    pole.append(input())
group = 1
for i in range(size):
    if i != size-1:         
        if pole[i] == pole[i+1]:
            group += 0
        else:
            group += 1
print(group)
