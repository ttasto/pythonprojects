import random

deck = [ 'Miss Scarlet', 'Colonel Mustard', 'Mrs. White', 'Reverend Green', 'Mrs. Peacock',
	'Professor Plum', 'Candlestick', 'Knife', 'Lead Pipe', 'Revolver', 'Rope', 'Wrench',
	'Ballroom', 'Billiard Room', 'Conservatory', 'Dining Room', 'Hall', 'Kitchen',
	'Library', 'Lounge', 'Study' ]

suspects = deck[0:6]
weapons = deck[6:12]
rooms = deck[12:21]
envelope = [ random.choice(suspects), random.choice(weapons), random.choice(rooms) ]

for cards in deck:
	if cards in envelope:
		deck.remove(cards)
random.shuffle(deck)

n_players = input("How many players (2-6) joining the game?: ")

while:
	if n_players == '2':
		hand1 = deck[0::2]
		hand2 = deck[1::2]

	elif n_players == '3':
		hand1 = [ deck[0::3] ]
		hand2 = [ deck[1::3] ]
		hand3 = [ deck[2::3] ]

	elif n_players == '4':
		hand1 = deck[0::4]
		hand2 = deck[1::4]
		hand3 = deck[2::4]
		hand4 = deck[3::4]

	elif n_players == '5':
		hand1 = deck[0::5]
		hand2 = deck[1::5]
		hand3 = deck[2::5]
		hand4 = deck[3::5]
		hand5 = deck[4::5]

	elif n_players == '6':
		hand1 = deck[0::6]
		hand2 = deck[1::6]
		hand3 = deck[2::6]
		hand4 = deck[3::6]
		hand5 = deck[4::6]
		hand6 = deck[5::6]

	else:
		print("Please enter a number (2-6).")
