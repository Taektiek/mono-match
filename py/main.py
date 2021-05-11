from random import shuffle

with open('py/emoji.txt', mode='r') as emoji_txt:
    emoji_encoded = set()
    for i in emoji_txt.read().split('\n'):
        emoji_encoded.add(i)

symbols = []
for i in emoji_encoded:
    symbols.append(chr(int(i[2:], 16)))

def generate_combinations(number_of_symbols, shuffle_symbols):
    cards = []

    #Work out the prime number
    n = number_of_symbols - 1

    #Total number of cards that can be generated following the Dobble rules
    numberOfCards = n**2 + n + 1  #e.g. 7^2 + 7 + 1 = 57


    #Add first set of n+1 cards (e.g. 8 cards)
    for i in range(n+1):  
        #Add new card with first symbol
        cards.append([1])
        #Add n+1 symbols on the card (e.g. 8 symbols)
        for j in range(n):
            cards[i].append((j+1)+(i*n)+1)

    #Add n sets of n cards 
    for i in range(0,n):
        for j in range(0,n):
            #Append a new card with 1 symbol
            cards.append([i+2])

            #Add n symbols on the card (e.g. 7 symbols)
            for k in range(0,n):
                val  = (n+1 + n*k + (i*k+j)%n)+1
                cards[len(cards)-1].append(val)

    #Shuffle symbols on each card
    if shuffle_symbols:
        for card in cards:
            shuffle(card)
        
    #Output all cards  
    emoji_cards = []
    for i, card in enumerate(cards):
        emoji_cards.append([symbols[j-1] for j in card])

    real_cards = []
    for i in emoji_cards:
        real_cards.append(''.join(i))

    shuffle(real_cards)

    return real_cards

combinations = generate_combinations(20, True)

with open('py/cards.txt', 'w', encoding="utf-8") as cards_txt:
    cards_txt.write('<div class="row hidden">' + '</div><div class="row hidden">'.join([''.join([f'<div class="emoji">{i}</div>' for i in combination]) for combination in combinations]) + '</div>')