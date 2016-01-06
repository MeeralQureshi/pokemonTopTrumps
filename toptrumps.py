import pokemon
import requests
import player
from random import randint
import time


def gen_number(used_numbers, deck):
    """
    Generate a random number between 1-151 and add the respective Pokemon to the deck if it is not already
    in the game deck.
    """
    number = randint(1, 151)
    while(number in used_numbers):
        number = randint(1,151)
    poke = pokemon.Pokemon(number)
    deck.append(poke)
    used_numbers.append(number)
    return deck

def print_card(card):
        """
        Prints the stats of the Pokemon "card"
        """

        print("Pokemon name: " + card.name)
        print("HP: " + str(card.hp))
        print("Attack: " + str(card.attack))
        print("Defense: " + str(card.defense))
        print("Speed: " + str(card.speed))
        print("Special Attack: " + str(card.special_attack))
        print("Special Defense: " + str(card.special_defense))


class Game:
    def __init__(self, player1, player2):
        """
        Create a game between two players
        """
        self.player1 = player1
        self.player2 = player2
        self.game_deck = []
        self.winner = None

    def create_deck(self, player1, player2):
        """
        Create a global deck and split it in half between the two players
        30 Cards being used in each game, 15 for each player
        """
        used_numbers = []
        for i in range(0, 30):
            self.game_deck = gen_number(used_numbers, self.game_deck)
        self.player1.create_deck(self.game_deck[:len(self.game_deck)//2])
        self.player2.create_deck(self.game_deck[len(self.game_deck)//2:])


    def check_stats(self, chosen_stat):
        """
        Checks the stats of the two players against each other and prints accordingly
        """

        if chosen_stat == "hp":
            higher = self.player1.compare_first_card(self.player2, "hp")
            if higher == self.player1:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou win the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player1 = self.player1.player_wins(self.player2)
                self.player2 = self.player2.player_loses()
                self.player1.won = True
                self.player2.won = False
                time.sleep(4)
            else:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou lose the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player2 = self.player2.player_wins(self.player1)
                self.player1 = self.player1.player_loses()
                self.player1.won = False
                self.player2.won = True
                time.sleep(4)


        elif chosen_stat == "attack":
            higher = self.player1.compare_first_card(self.player2, "attack")
            if higher == self.player1:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou win the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player1 = self.player1.player_wins(self.player2)
                self.player2 = self.player2.player_loses()
                self.player1.won = True
                self.player2.won = False
                time.sleep(4)

            else:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou lose the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player2 = self.player2.player_wins(self.player1)
                self.player1 = self.player1.player_loses()
                self.player1.won = False
                self.player2.won = True
                time.sleep(4)

        elif chosen_stat == "defense":
            higher = self.player1.compare_first_card(self.player2, "defense")
            if higher == self.player1:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou win the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player1 = self.player1.player_wins(self.player2)
                self.player2 = self.player2.player_loses()
                self.player1.won = True
                self.player2.won = False
                time.sleep(4)
            else:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou lose the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player2.player_wins(self.player2)
                self.player1 = self.player1.player_loses()
                self.player1.won = False
                self.player2.won = True
                time.sleep(4)

        elif chosen_stat == "speed":
            higher = self.player1.compare_first_card(self.player2, "speed")
            if higher == self.player1:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou win the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player1 = self.player1.player_wins(self.player2)
                self.player2 = self.player2.player_loses()
                self.player1.won = True
                self.player2.won = False
                time.sleep(4)
            else:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou lose the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player2 = self.player2.player_wins(self.player1)
                self.player1 = self.player1.player_loses()
                self.player1.won = False
                self.player2.won = True
                time.sleep(4)

        elif chosen_stat == "special attack":
            higher = self.player1.compare_first_card(self.player2, "special attack")
            if higher == self.player1:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou win the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player1 = self.player1.player_wins(self.player2)
                self.player2 = self.player2.player_loses()
                self.player1.won = True
                self.player2.won = False
                time.sleep(4)

            else:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou lose the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player2 = self.player2.player_wins(self.player1)
                self.player1 = self.player1.player_loses()
                self.player1.won = False
                self.player2.won = True
                time.sleep(4)

        elif chosen_stat == "special defense":
            higher = self.player1.compare_first_card(self.player2, "special defense")
            if higher == self.player1:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou win the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player1 = self.player1.player_wins(self.player2)
                self.player2 = self.player2.player_loses()
                self.player1.won = True
                self.player2.won = False
                time.sleep(4)

            else:
                print("\nHere is your opponent's card: \n")
                print_card(self.player2.deck[0])
                print("\nYou lose the round!\n")
                print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
                self.player2 = self.player2.player_wins(self.player1)
                self.player1 = self.player1.player_loses()
                self.player1.won = False
                self.player2.won = True
                time.sleep(4)

        else:
            print("\n!! That is not a valid trump!! \n")
            self.player_turn()

        if len(self.player1.deck) == 0:
            print(self.player2.name + " has all the cards\n")
            print(self.player2.name + " wins!")
            self.winner = self.player2

        if len(self.player2.deck) == 0:
            print(self.player1.name + " has all the cards\n")
            print(self.player1.name + " wins!")
            self.winner = self.player1

    def player_turn(self):
        """
        Allow the player to play their turn
        """
        print("You have " + str(len(self.player1.deck)) +  " cards")
        print(self.player2.name + " has " + str(len(self.player2.deck)) +  " cards")
        print("Here is your top card\n")
        print_card(self.player1.deck[0])
        print("\nPlease choose a trump stat from the following hp, attack, defense, speed, special attack, "
              "special defense\n")
        chosen_stat = input("Please enter your chosen stat: ")

        self.check_stats(chosen_stat)


    def computer_turn(self):
        """
        Allow the computer to play their turn and pick a random trump against the player
        """
        print("You have " + str(len(self.player1.deck)) +  " cards")
        print(self.player2.name + " has " + str(len(self.player2.deck)) +  " cards")
        print("Here is your top card\n")
        print_card(self.player1.deck[0])
        print("\nYour opponent is choosing a trump stat")
        rand_num = randint(1, 6)
        chosen_stat = None

        if rand_num == 1:
            chosen_stat = "hp"
        elif rand_num == 2:
            chosen_stat = "attack"
        elif rand_num == 3:
            chosen_stat = "defense"
        elif rand_num == 4:
            chosen_stat = "speed"
        elif rand_num == 5:
            chosen_stat = "special attack"
        else:
            chosen_stat = "special defense"
        time.sleep(2)
        print("\n Your opponent picked " + chosen_stat + "!\n")

        self.check_stats(chosen_stat)

# Start the game
print("~~ Welcome to the Pokemon Top Trumps Game! ~~ \n")
player1name = input("Player 1, please enter your name: ")
print("Hello " + player1name + ", get ready to enter the world of Pokemon!\n")
computername = "Computer"
print("You are playing against " + computername +  ", get ready...\n")

# Create players
player1 = player.Player(player1name)
computer = player.Player(computername)

game = Game(player1, computer)

# Keep alternating turns until someone wins
# Whoever wins the round gets to pick another trump
game.create_deck(player1, computer)
while game.winner == None:
    game.player_turn()
    while game.player1.won:
        game.player_turn()
        if game.winner != None:
            break
    if game.winner == None:
        game.computer_turn()
        while game.player2.won:
            game.computer_turn()
        if game.winner != None:
            break

print("Game over!")


