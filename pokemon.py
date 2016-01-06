import requests
import ast


class Pokemon:
    """
    Pokemon class with name, hp, attack, defense, speed, special attack and special defense
    """
    def __init__(self, number):
        """
        Creates a pokemon by sending a request to the API

        :param number: Takes the number of a pokemon (From 1 - 151)
        """
        pokemonreq = requests.get('http://pokeapi.co/api/v1/pokemon/' + str(number) + '/')
        pokemondict = pokemonreq.text
        pokemon = ast.literal_eval(pokemondict)
        self.name = pokemon["name"]
        self.hp = pokemon["hp"]
        self.attack = pokemon["attack"]
        self.defense = pokemon["defense"]
        self.speed = pokemon["speed"]
        self.special_attack = pokemon["sp_atk"]
        self.special_defense = pokemon["sp_def"]

    def compare(self, other, stat):
        """
        Takes two pokemon "cards" and compares the chosen stat

        :param other: Other player
        :param stat: The stat to be compared
        :return: The Pokemon "card" that won the comparison
        """
        if stat == "hp":
            if self.hp >= other.hp:
                return 0
            else:
                return 1
        elif stat == "attack":
            if self.attack >= other.attack:
                return 0
            else:
                return 1
        elif stat == "defense":
            if self.defense >= other.defense:
                return 0
            else:
                return 1
        elif stat == "speed":
            if self.speed >= other.speed:
                return 0
            else:
                return 1
        elif stat == "special attack":
            if self.special_attack >= other.special_attack:
                return 0
            else:
                return 1
        else:
            if self.special_defense >= other.special_defense:
                return 0
            else:
                return 1

