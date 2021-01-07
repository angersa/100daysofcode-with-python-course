import random


class Player():
    def __init__(self, name):
        self.name = name


class Roll():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def can_defeat(self, roll):
        paires = {
            'roche': 'ciseau',
            'papier': 'roche',
            'ciseau': 'papier',
            }           
        p1_roll = self.name
        p2_roll = roll.name
        if paires[p1_roll] == p2_roll:
            return 1
        elif paires[p2_roll] == p1_roll:
            return -1
        else:
            return 0


def main():
    print_header()

    rolls = [
        'roche',
        'papier',
        'ciseau',
    ]

    name = input("Votre nom: ")

    player1 = Player(name)
    player2 = Player("computer")

    game_loop(player1, player2, rolls)


def print_header():
    print('--------------------------------')
    print('      ROCHE PAPIER CISEAU')
    print('--------------------------------')
    print()


def get_p1_choice():
    choix = {'r': 'roche', 'p': 'papier', 'c': 'ciseau'}
    entry = input('[r]oche, [p]apier, [c]iseau?')
    return choix[entry]


def game_loop(player1, player2, rolls):
    count = 0
    score = 0
    while count < 3:
        p2_roll = Roll(random.choice(rolls))
        p1_roll = Roll(get_p1_choice())

        outcome = p1_roll.can_defeat(p2_roll)
        score += outcome

        # display throws
        print(f'{player1.name.title()} : {p1_roll}')
        print(f'Computer : {p2_roll}')
        # display winner for this round
        if outcome == 1:
            print(f"{player1.name.title()} l'emporte!")
        elif outcome == -1:
            print(f"{player2.name.title()} l'emporte!")
        else:
            print("Partie nulle.")

        count += 1

    # Compute who won
    print(f"Score final : {score}")
    if score > 0:
        print(f"{player1.name.title()} gagne le match!")
    elif score < 0:
        print(f"{player2.name.title()} gagne le match!")
    else:
        print('Match nul.')


if __name__ == "__main__":
    main()