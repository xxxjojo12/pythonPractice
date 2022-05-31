a, b = map(float, input().split())

if a < 150:
    c = a - 100
elif 150 <= a < 160:
    c = ((a - 150)/2)+50
elif 160 <= a:
    c = (a - 100)*0.9

d = (b - c)*100/c

if d <= 10:
    print("정상")
elif 10 <d <= 20:
    print("과체중")
elif 20 < d:
    print("비만")