import random
from itertools import combinations

import combo

num = list(range(1, 10))

def check_sum(numbers):
    for combo in combinations(numbers, 3):
        if sum(combo) == 15:
            return combo


player1_numbers = []
while num:
    player1 = random.choice(num)
    player1_numbers.append(player1)
    num.remove(player1)
    print("Player 1 picks:", player1)

    combo = check_sum(player1_numbers)
    if combo:
        print("Player 1 wins with numbers:", combo[0], "+", combo[1] ,"+", combo[2] ,"=", sum(combo) )
        break

    if not num:
        print("It's a draw!")
        break
    player2_numbers = []
    player2 = random.choice(num)
    player2_numbers.append(player2)
    num.remove(player2)
    print("Player 2 picks:", player2)

    combo = check_sum(player2_numbers)
    if combo:
        print("Player 2 wins with numbers:",  combo[0] ,"+" ,combo[1], "+", combo[2], "=", sum(combo))
        break

    if not num:
        print("It's a draw!")
        break
