a, b = map(float, input().split())

avg_weight = (a-100)*0.9
bb = (b-avg_weight)*100/avg_weight

if bb <= 10:
    print("정상")
elif 10 < bb <= 20:
    print("과체중")
else:
    print("비만")