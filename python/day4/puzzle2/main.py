from total_scratchcards import parse_input, gather_cards

if __name__ == '__main__':
    with open('my_input.txt') as f:
        inp = f.read()
    cards = parse_input(inp)
    cards_and_counts = gather_cards(cards)
    s = sum([count for card, count in cards_and_counts])
    print(s)