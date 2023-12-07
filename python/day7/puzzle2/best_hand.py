def parse_input(input_str):
    cards = []
    hands = input_str.splitlines()
    hands = [hand.strip() for hand in hands]
    for hand in hands:
        [hand, bid] = hand.split()
        cards.append((hand, bid))
    return cards

def hand_type(hand):
    count = {}
    for card in hand:
        if card in count:
            count[card] += 1
        else:
            count[card] = 1

    # Transforming jokers
    if 'J' in count and len(count) > 1:
        joker_count = count['J']
        del count['J']
        most_common_card = max(count, key=count.get)
        count[most_common_card] += joker_count
    
    if len(count) == 1:
        return 1
    elif len(count) == 2:
        if 4 in count.values():
            return 2
        else:
            return 3
    elif len(count) == 3:
        if 3 in count.values():
            return 4
        else:
            return 5
    elif len(count) == 4:
        return 6
    else:
        return 7
    
def is_better_card(card1, card2):
    cards = "AKQT98765432J"
    return cards.index(card1) < cards.index(card2)

def is_better_hand(hand1, hand2):
    type_1 = hand_type(hand1)
    type_2 = hand_type(hand2)
    if type_1 < type_2:
        return True
    elif type_1 > type_2:
        return False
    else:
        for c1, c2 in zip(hand1, hand2):
            if c1 != c2:
                return is_better_card(c1, c2)
            
def sorted_hands(hands):
    desc_sorted_hands = [hands[0]]
    for hand in hands[1:]:
        for i in range(len(desc_sorted_hands)):
            if is_better_hand(hand[0], desc_sorted_hands[i][0]):
                desc_sorted_hands.insert(i, hand)
                break
        else:
            desc_sorted_hands.append(hand)
    return desc_sorted_hands

def dicho_sorted_hands(hands):
    desc_sorted_hands = [hands[0]]
    for hand in hands[1:]:
        start = 0
        end = len(desc_sorted_hands) - 1
        while start <= end:
            mid = (start + end) // 2
            if is_better_hand(hand[0], desc_sorted_hands[mid][0]):
                end = mid - 1
            else:
                start = mid + 1
        desc_sorted_hands.insert(start, hand)
    return desc_sorted_hands

if __name__ == '__main__':
    my_cards = parse_input("32T3K 765\nT55J5 684\nKK677 28\nKTJJT 220\nQQQJA 483")
    for card in my_cards:
        print(hand_type(card[0]))
    # print(is_better_hand(my_cards[0][0], my_cards[1][0]))
    # print(is_better_hand(my_cards[1][0], my_cards[2][0]))
    print(dicho_sorted_hands(my_cards))
    
