from sys import stdin

lotto_nums = stdin.readline().rstrip().split()

jihye_nums = stdin.readline().rstrip().split()

winning_nums = lotto_nums[:6]
bonus_nums = lotto_nums[-1]

winning_num_cnt = 0

bonused = False

for jihye_num in jihye_nums:
    if jihye_num in winning_nums:
        winning_num_cnt += 1

if bonus_nums in jihye_nums:
    bonused = True

if winning_num_cnt == 6:
    print(1)
elif winning_num_cnt == 5 and bonused:
    print(2)
elif winning_num_cnt == 5:
    print(3)
elif winning_num_cnt == 4:
    print(4)
elif winning_num_cnt == 3:
    print(5)
else:
    print(0)