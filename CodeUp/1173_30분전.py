hour, min = map(int, input().split())

hTM = hour * 60
hPM = hTM + min
pasS = hPM - 30

hour = pasS // 60
min = pasS % 60
if hour < 0:
    print(hour+24, min)
else:
    print(hour, min)
