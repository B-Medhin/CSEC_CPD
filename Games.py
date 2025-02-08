num_g =int(input())
num_gu = 0
nums=[]

for i in range(num_g):
    num = list(map(int,input().split()))
    nums.append(num)
for i in range(num_g):
    for j in range(num_g):
        if nums[i][0] == nums[j][1]:
            num_gu +=1
print(num_gu)
