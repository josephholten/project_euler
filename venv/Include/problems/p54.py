# poker hand evaluation

from enum import Enum

SUITS = {"H": 1, "C": 2, "S": 3, "D": 4}
CARD_VALUE = {"T": 10, "J": 11, "Q": 12, "K": 13, "A": 14}

def convertCard(card):
    global SUITS
    global CARD_VALUE
    try:
        return int(card[0]),SUITS[card[1]]
    except ValueError:
        return CARD_VALUE[card[0]],SUITS[card[1]]

def sort_by_suit(hand):
    hand_split = [[],[],[],[]]
    hand_sorted = []
    for card in hand:
        hand_split[card[1]-1].append(card)
    for i, suit in enumerate(hand_split):
        hand_split[i] = sorted(suit, key = lambda x: x[0])
    for suit in hand_split:
        for card in suit:
            hand_sorted.append(card)
    return hand_sorted

def sort_by_value(hand):
    hand_split = []
    for i in range(14):
        hand_split.append([])
    hand_sorted = []
    for card in hand:
        hand_split[card[0]-1].append(card)
    for i, suit in enumerate(hand_split):
        hand_split[i] = sorted(suit, key = lambda x: x[1])
    for suit in hand_split:
        for card in suit:
            hand_sorted.append(card)
    return hand_sorted

def isStraight(hand):
    for i, card in enumerate(hand):
        if not card[0]+1 == hand[i+1][0]:
            return False
    return True

def nOfaKind(hand):
    hand = sort_by_value(hand)
    amount_of_type = []
    for i in range(14):
        amount_of_type.append([i+1, 0])
    for card in hand:
        amount_of_type[card[0]-1][1] += 1
    return sorted([l for l in amount_of_type if l[1] != 0], reverse=True, key=lambda x:x[1])

def high_card_eval(hands):
    for i in range()

    for card in hands[0]:
        if card[0] == m:
            return 1
    return 2

def getRank(hand):
    flush = True
    for card in hand:                   # check if same suit
        if not hand[0][1] == card[1]:
            flush = False
    if flush:
        hand = sort_by_suit(hand)
        if hand[0][0] == 10:
            return 10 # royal flush
    straight = isStraight(hand)
    if straight and flush:
        return 9 # straight flush
    n = nOfaKind(hand)   # returns a list of "tuples" (actually lists) with card value and amount pairs
    print("n:",n)
    if n[0][1]== 4:
        return 8 # four of a kind
    if n[0][1] == 3 and n[1][1] == 2:
            return 7 # full house
    if flush:
        return 6 # flush
    if straight:
        return 5 # straight
    if n[0][1] == 3:
        return 4 # three of a kind
    if n[0][1] == 2:
        if n[1][1] == 2:
            return 3 # two pairs
        return 2    # one pair
    return 1        # high card

def findWinner(hands):
    rank1 = getRank(hands[0])
    rank2 = getRank(hands[1])
    print("ranks:",rank1, rank2)
    if rank1 > rank2:
        return 1
    if rank2 > rank1:
        return 2
    if rank1 in [8,7,4,3,2]:
        n1 = nOfaKind(hands[0])
        n2 = nOfaKind(hands[1])
        if rank1 == 2:
            return high_card_eval(hands)
        for i in range(2):
            if n1[i][0] > n2[i][0]:
                return 1
            if n1[i][0] < n2[i][0]:
                return 2



with open("p054_poker.txt", "r") as p_h_file:
    hands = p_h_file.readlines()            # hands: number, player, card, (value, suit)
    for hand_n in range(len(hands)):
        hands[hand_n]=[hands[hand_n][:15],hands[hand_n][15:]]
        for player in range(2):
            hands[hand_n][player] = hands[hand_n][player].strip()     # removed new line characters
            hands[hand_n][player] = hands[hand_n][player].split()
            for i, card in enumerate(hands[hand_n][player]):
                hands[hand_n][player][i] = convertCard(card)
    #print(hands)
    #for hand in hands[:15]:
    hand1 = [(5,1),(5,2),(6,3),(7,3),(13,4)]
    hand2 = [(2,2),(3,3),(8,3),(8,4),(10,4)]
    #print(getRank(hand1), getRank(hand2))
    print(findWinner(hands[0]))
