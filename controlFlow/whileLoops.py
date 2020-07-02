# While loops are an example of "indefinite iteration" which is when a loop repeats an unknown number of times and ends when some condition is met

card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

while sum(hand) < 17:
    hand.append(card_deck.pop())

print(hand)

# Factorials with While Loops
# A factorial of a whole number is that number multiplied by every whole number between itself and 1
# For ex, 6 factorial (written 6!) equals 6 x 5 x 4 x 3 x 2 x 1 - 720
