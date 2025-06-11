# -*- coding: utf-8 -*-
"""
Created on Wed Jun 11 10:10:32 2025

@author: prakh
"""

def FindPockerHand(hand):

    ranks = []
    suits = []
    pockerhand = {10: "Royal Flush", 9: "Straight Flush", 8: "Four Of A Kind", 7: "Full House", 6: "Flush", 5: "Straight", 4: "Three Of A Kind", 3: "Two Pair", 2: "Pair", 1: "High Card"}
    possiblehand = []
    for card in hand:
        if len(card) == 2:
            rank = card[0]
            suit = card[1]
        else:
            rank = card[0:2]
            suit = card[2]

        if rank == 'A':
            rank = 14
        elif rank == 'K':
            rank = 13
        elif rank == 'Q':
            rank = 12
        elif rank == 'J':
            rank = 11
        ranks.append(int(rank))
        suits.append(suit)

    sortedranks = sorted(ranks)

    # Royal Flush AND Straight flush AND Flush
    if suits.count(suits[0]) == 5:  # Checking For Flush
        if 14 in sortedranks and 13 in sortedranks and 12 in sortedranks and 11 in sortedranks and 10 in sortedranks:
            possiblehand.append(10)

        elif all(sortedranks[i] == sortedranks[i-1] + 1 for i in range(1,5)):
            possiblehand.append(9)
        else:
            possiblehand.append(6)

    # Straight
    if all(sortedranks[i] == sortedranks[i-1] + 1 for i in range(1,5)):
        possiblehand.append(5)

    uniquehandvalue = list(set(sortedranks))

    # Four Of A Kind AND Full House
    if len(uniquehandvalue) == 2:
        for val in uniquehandvalue:
            if sortedranks.count(val) == 4:
                possiblehand.append(8)
            if sortedranks.count(val) == 3:
                possiblehand.append(7)

    # Three Of A Kind And Two Pair
    if len(uniquehandvalue) == 3:
        for val in uniquehandvalue:
            if sortedranks.count(val) == 3:
                possiblehand.append(4)
            if sortedranks.count(val) == 2:
                possiblehand.append(3)

    # Pair
    if len(uniquehandvalue) == 4:
        possiblehand.append(2)
    if not possiblehand:
        possiblehand.append(1)

    return pockerhand[max(possiblehand)]

if __name__=="__main__":
    PockerHand(["KH", "AH", "QH", "JH", "10H"])  # ROYAL FLUSH
    PockerHand(["QC", "JC", "10C", "9C", "8C"])  # STRAINGHT FLUSH
    PockerHand(["5C", "5S", "5H", "5D", "QH"])  # FOUR OF KIND
    PockerHand(["2H", "2D", "2S", "10H", "10C"])  # FULL HOUSE
    PockerHand(["2D", "KD", "7D", "6D", "5D"])  # FLUSH
    PockerHand(["JC", "10H", "9C", "8C", "7D"])  # STRAIGHT
    PockerHand(["10H", "10C", "10D", "2D", "5S"])  # THREE OF A KIND
    PockerHand(["KD", "KH", "5C", "5S", "6D"])  # TWO PAIR
    PockerHand(["2D", "2S", "9C", "KD", "10C"])  # PAIR
    PockerHand(["KD", "5H", "2D", "10C", "JH"])  # HIGH CARD

