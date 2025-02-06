amount = int(input())
color =(input())
count = 0
j = amount - 1
for i in range(amount):
    if i != j:
        if color[i]== color[i+1]:
          count +=1
          
print(count)
