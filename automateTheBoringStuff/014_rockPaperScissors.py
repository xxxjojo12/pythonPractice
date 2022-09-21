import sys, random

print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0


while 1:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))

    while 1:
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        me = input()

        if me == 'q':
            sys.exit()
        if me == 'r' or me == 'p' or me == 's':
            break
        print('Type one of r, p, s, or q.')

#Display what the player chose:
    if me == 'r':
        print('Rock versus...')
    elif me == 'p':
        print('Paper versus...')
    elif me == 's':
        print('Scissors versus...')

    #Display what the computer chose:
    vs = random.randint(1, 3)
    if vs == 1:
        vss = 'r'
        print('ROCK')
    elif vs == 2:
        vss = 'p'
        print('PAPER')
    elif vs == 3:
        vss = 's'
        print('SCISSORS')

    #Display and record the win/loss/tie:
    if me == vss:
        print('It is a tie!')
        ties += 1
    elif me == 'r' and vss == 's':
        print('You win!')
        wins += 1
    elif me == 'r' and vss == 'p':
        print('You lose!')
        losses += 1
    elif me == 'p' and vss == 'r':
        print('You win!')
        wins += 1
    elif me == 'p' and vss == 's':
        print('You lose!')
        losses += 1
    elif me == 's' and vss == 'r':
        print('You lose!')
        losses += 1
    elif me == 's' and vss == 'p':
        print('You win!')
        wins += 1