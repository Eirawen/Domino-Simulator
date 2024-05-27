
import random 
from typing import List
from collections import defaultdict 


class DominoSide:
    def __init__(self, value):
        self.value = value
        self.used = False

    def use(self):
        self.used = True

    def __str__(self):
        return str(self.value)
    
class Domino:
    def getSideValue(self, side):
        return side.value
    def getSides(self):
        return [self.side1, self.side2]

    def __init__(self, side1, side2):
        self.side1 = DominoSide(side1)
        self.side2 = DominoSide(side2)
    

def generate_dominoes():
    dominoes = []
    for i in range(7):
        for j in range(i, 7):
            dominoes.append(Domino(i, j))
    return dominoes

def generate_hand(dominoes: List[Domino], handSize: int) -> List[Domino]:
    hand = []
    for i in range(handSize):
        hand.append(dominoes.pop(random.randint(0, len(dominoes) - 1)))
    return hand 

def is_valid_connection(domino1: Domino, domino2: Domino) -> bool:
    if domino1.side1.value == domino2.side1.value and not domino1.side1.used and not domino2.side1.used:
        domino1.side1.use()
        domino2.side1.use()
        return True
    if domino1.side1.value == domino2.side2.value and not domino1.side1.used and not domino2.side2.used:
        domino1.side1.use()
        domino2.side2.use()
        return True
    if domino1.side2.value == domino2.side1.value and not domino1.side2.used and not domino2.side1.used:
        domino1.side2.use()
        domino2.side1.use()
        return True
    if domino1.side2.value == domino2.side2.value and not domino1.side2.used and not domino2.side2.used:
        domino1.side2.use()
        domino2.side2.use()
        return True
    return False


def max_length(dominoes: List[Domino]) -> List[Domino]:
    max_length = 0
    max_length_dominoes = []

    def search(current_chain: List[Domino], remaining_dominoes: List[Domino]):
        if not remaining_dominoes:
            return current_chain
        max_chain = current_chain

        for i in range(len(remaining_dominoes)):
            if is_valid_connection(current_chain[-1], remaining_dominoes[i]):
                new_chain = search(current_chain + [remaining_dominoes[i]], remaining_dominoes[:i] + remaining_dominoes[i+1:])
                if len(new_chain) > len(max_chain):
                    max_chain = new_chain
        return max_chain
    max_chain = [] 
    for i in range(len(dominoes)):
        chain = search([dominoes[i]], dominoes[:i] + dominoes[i+1:])
        if len(chain) > len(max_chain):
            max_chain = chain
    max_length = len(max_chain)
    max_length_dominoes = max_chain
    return max_length, max_length_dominoes


def monte_carlo_simulation(dominoes: List[Domino], num_simulations: int, hand_size: int) -> List[Domino]:
    max_length_dominoes = []
    max_length = 0


    for _ in range(num_simulations):
        dominoes_copy = generate_dominoes()
        hand = generate_hand(dominoes_copy, hand_size)
        length, cur_dominoes = max_length(hand)
        if length > max_length:
            max_length = length
            max_length_dominoes = cur_dominoes
    return max_length, max_length_dominoes


def domino_print(dominoes: List[Domino]):
    for domino in dominoes:
        print(f"{domino.side1} {domino.side2}") 


def main():
    dominoes = generate_dominoes()
    
    handToMax = {} 
    hand = generate_hand(dominoes, 14)
    domino_print(hand)
    length, max_length_dominoes = max_length(hand)
    print(f"Max length: {length}")
    domino_print(max_length_dominoes)



    



if __name__ == "__main__":
    main()


