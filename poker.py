

# Below is an array of strings that represents a random assortment of 5 poker hands. 
# The first number or letter represents the face value of each card.
# The second letter represent the suit of each card. 

test_hands = [
    ["AC", "5C", "10C", "7C", "3S"],
    ["2C", "3D", "4S", "5H", "2D"],
    ["2C", "3D", "4S", "3H", "2D"],
    ["5S", "4C", "AD", "4S", "4H"],
    ["3H", "7H", "6S", "4D", "5S"],
    ["AC", "5C", "10C", "7C", "3C"],
    ["5C", "8D", "5H", "8S", "8H"],
    ["3D", "7H", "7S", "7C", "7D"],
    ["AS", "10S", "QS", "KS", "JS"],
]

def suit(card): # This function defines the suit of a card. 
    return card[-1] 

def value(card):    # This function defines the value of each card.
    if card [0] =="A":
        return 14
    if card [0] =="K":
        return 13
    if card [0] =="Q":
        return 12
    if card [0] =='J':
        return 11
    return int(card[0:-1])

def is_flush(cards): # This function defines a 5 card flush.
        return all([suit(card) == suit(cards[0])] for card in cards[1:]])

def hand_dist(cards):
    dist = {i:0 for i in range(1,15)}
    for card in cards:
        dist[value(card)] += 1
    dist[1] = dist[14] # The Ace is given lowest and highest 
    return dist

def straight_high_card(cards): # This function defines a 5 card straight.
  dist = hand_dist(cards)
  for value in range(1, 11):
    if all([dist[value + k] == 1 for k in range(5)]):
      return value + 4


      
  



    
