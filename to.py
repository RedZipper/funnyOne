#!/usr/bin/python2

import random

### 21 ####
cards = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
'2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC',
'2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', '10H', 'JH', 'QH', 'KH', 'AH',
'2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', '10S', 'JS', 'QS', 'KS', 'AS']

#print cards    

def shuffle():
	
	random.shuffle(cards)
	return cards

def deal(deck):
	
	mcards = []
	mcards.append(deck.pop())
	mcards.append(deck.pop())
	return mcards

def peek(hand):
	print "Your Hand: ",  hand


#return number on success 10 on failure
def calcValue(val,curSum):
	
	try:
		num =  int(val)
		return num

	#not a number
	except ValueError:
		
		if val != 'A': 
			# J Q K
#			print "returning 10"
			return 10
		
		elif curSum <= 10:
#			 print "returning 11"
			 return 11

		elif curSum >= 11:
#			print "returning 1"
			return 1	

def sumHand(f, s):

	return f+s

def calculateHand(hand):

	val = 0
	for card in xrange(len(hand)):
		aCard = hand[card][0]
#		print "card: " + aCard + "\n"
		val += calcValue(aCard, val)
		
	return val

def hitMe(deck, mcards):
	
	keepHitting = True

	while keepHitting:
		mcards.append(deck.pop())
		peek(mcards)
		
		mSum = calculateHand(mcards)
		
		if mSum > 21:
			keepHitting = False
			return mSum
		
		ans = raw_input("Hit again? ")
		
		if (ans != 'Y') or  (ans != 'y'):
			keepHitting = False	
	
	return mSum


deck = [] 

deck  = shuffle()

#print 'The deck after shuffling: ' , deck

mhand = []
cpuhand = []

mhand = deal(deck) 
cpuhand = deal(deck)

hSum = calculateHand(mhand)
pSum = calculateHand(cpuhand)

print 'My hand:',  mhand, hSum
print 'Computer\'s Hand', cpuhand, pSum

if hSum == 21:
	print "Winner 21!" 
elif hSum < pSum and hSum < 21:

	ans = raw_input("Hit?: ")

	if str(ans) == 'Y' or str(ans) == 'y':
		hSum = hitMe(deck, mhand)  
		
		if hSum > 21:
			print "You Lose!"
		elif hSum == 21:
			print "Winner 21!"
	else:	
		print "Game Over!"

print mhand
