import math
Y, W = map(int, input().split())
max_roll = max(Y, W)
if max_roll > 6:
    winning_outcomes = 0
else:
    winning_outcomes = 7 - max_roll
total_outcomes = 6
numerator = winning_outcomes
denominator = total_outcomes
if numerator == 0:
    print("0/1")
elif numerator == denominator:
    print("1/1")
else:
    gcd = math.gcd(numerator, denominator)
    print(f"{numerator // gcd}/{denominator // gcd}")
