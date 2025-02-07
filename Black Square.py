calo_num = list(map(int,input().split()))
strip = input()
tot_calo = 0

for i in strip:
    if i == "1":
        tot_calo += calo_num[0]
    elif i == "2":
        tot_calo += calo_num[1]
    elif i == "3":
        tot_calo += calo_num[2]
    elif i == "4":
        tot_calo += calo_num[3]
print(tot_calo)
