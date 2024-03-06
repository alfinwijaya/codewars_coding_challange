def rps(p1, p2):
    return ('Draw!' if p1 == p2 
            else 'Player 1 won!' if (p1 == 'scissors' and p2 == 'paper') or
                                    (p1 == 'rock' and p2 == 'scissors') or
                                    (p1 == 'paper' and p2 == 'rock')
            else 'Player 2 won!'
        )

print(rps('rock', 'scissors'))
print(rps('scissors', 'rock'))
print(rps('rock', 'rock'))