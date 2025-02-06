size = int(input())
card = list(map(int, input().split()))
Sereja = 0
Dima = 0
j = size - 1

for i in range(size):
    if card[0] >= card[j]:  
        if i % 2 == 0:  
            Sereja += card[0]
        else:  
            Dima += card[0]
        card.pop(0)
        j -= 1
    else:  
        if i % 2 == 0: 
            Sereja += card[j]
        else:  
            Dima += card[j]
        card.pop(j)  
        j -= 1  

print(Sereja, Dima)
