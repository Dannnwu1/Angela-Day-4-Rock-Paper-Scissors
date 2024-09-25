from art import rock, paper, scissors
from random import randint


def art(a):
    if a == 0:
        return rock
    elif a == 1:
        return paper
    elif a == 2:
        return scissors


def winner(d, e):
    if d == 0 and e == 2:
        return d
    elif d == e:
        return -1
    elif (e == 0 and d == 1) or (d == 2 and e == 1):
        return d


def compare(b, c):
    if b == winner(b, c):
        print("You win!")
    elif winner(b, c) == -1:
        print("It's a draw!")
    else:
        print("You lose!")


def game():
    uc = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))
    print(art(uc))
    cc = randint(0, 2)
    print(f"Computer's choice is {cc}.")
    print(art(cc))
    compare(uc, cc)


while True:
    game()
