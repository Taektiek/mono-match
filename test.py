symbols = ['a', 'b', 'c', 'd']

cards = [[1, 2, 3, 4], [4, 3, 2, 1], [1, 4, 2, 3], [3, 2, 1, 4]]

emoji_cards = []
for i, card in enumerate(cards):
    emoji_cards.append([symbols[j-1] for j in card])

print(emoji_cards)