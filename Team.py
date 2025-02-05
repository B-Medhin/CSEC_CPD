num_prob = int(input())
sure_solution = 0
for i in range(num_prob):
    p,v,t = map(int,input().split())
    if p+v+t >= 2:
        sure_solution += 1
print(sure_solution)
