input = open("input.txt").readlines()

card_values = {
  "A": 14, 
  "K": 13,
  "Q": 12,
  "J": 1,
  "T": 10,
  "9": 9,
  "8": 8,
  "7": 7,
  "6": 6,
  "5": 5,
  "4": 4,
  "3": 3,
  "2": 2
}

class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = bid

    def getCardTypeValue(self):
        card_count = {}
        jokers = 0
        for char in list(self.cards):
            if char == "J":
                jokers += 1
                continue
            if char not in card_count.keys():
                card_count[char] = 0
            card_count[char] += 1
        if len(card_count.keys()) > 0:
            card_most = list(card_count.keys())[0]
            for card in card_count.keys():
                if card_count[card] > card_count[card_most]:
                    card_most = card
            card_count[card_most] += jokers
        else:
            return 6
        if len(card_count.keys()) == 1:
            return 6
        if len(card_count.keys()) == 2:
            if card_count[list(card_count.keys())[0]] == 4 or card_count[list(card_count.keys())[1]] == 4:
                return 5
            return 4
        if len(card_count.keys()) == 3:
            for count in card_count.values():
                if count == 3:
                    return 3
            return 2
        if len(card_count.keys()) == 4:
            return 1
        return 0

    def worthMore(self, otherHand):
        if self.getCardTypeValue() == otherHand.getCardTypeValue():
            for i in range(5):
                if card_values[self.cards[i]] == card_values[otherHand.cards[i]]:
                    continue
                return card_values[self.cards[i]] > card_values[otherHand.cards[i]]
        else:
            return self.getCardTypeValue() > otherHand.getCardTypeValue()

    def __repr__(self):
        return self.cards

hands = []
for line in input:
    cards = line.split(" ")[0]
    bids = int(line.split(" ")[1])
    hand = Hand(cards, bids)
    if len(hands) == 0:
        hands.append(hand)
        continue

    success = False
    for index, contestant_hand in enumerate(hands):
        if hand.worthMore(contestant_hand):
            hands.insert(index, hand)
            success = True
            break
    if not success:
        hands.append(hand)
hands.reverse()

result = 0
for index, hand in enumerate(hands):
    result += (index + 1) * hand.bid
print(f"Result: {result}")
