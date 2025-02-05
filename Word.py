word = list(input())
upp=0
low=0 
for i in word:
    if i.isupper():
        upp+=1
    else:
        low+=1

if upp <= low:
    print(''.join(word).lower())  
else:
    print(''.join(word).upper())
