from best_hand import parse_input, sorted_hands, dicho_sorted_hands
import time

if __name__ == '__main__':
    with open("my_input.txt", "r") as f:
        my_input = f.read()
    start = time.perf_counter()
    my_cards = parse_input(my_input)
    # my_cards = sorted_hands(my_cards)
    my_cards = dicho_sorted_hands(my_cards)
    s = 0
    for i, hand in enumerate(my_cards):
        s += (len(my_cards) - i) * int(hand[1])
    print(s)
    print(f"Time: {time.perf_counter() - start}")