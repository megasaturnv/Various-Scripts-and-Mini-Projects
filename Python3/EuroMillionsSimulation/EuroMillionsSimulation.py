#!/usr/bin/python3
import random, time

#Settings
verbose = True
startingMoney = 100
priceOfTicket = 1.74 # Should be £2.50, but £0.76 goes into Millionaire Maker so we'll say a EuroMillions ticket costs £1.74
jackpot = 124819178 # Jackpot on 02 May 2023


# Global Variables
week = 0
totalTicketsPurchased = 0
bestWinnings = 0
money = startingMoney
winningsAndOdds = { # Main Number # _ Lucky Star # : [ winnings , probability ]
	'MN2_LS0': [3,22],
	'MN2_LS1': [5,49],
	'MN1_LS2': [6,188],
	'MN3_LS0': [8,314],
	'MN3_LS1': [9,706],
	'MN2_LS2': [12,985],
	'MN4_LS0': [33,13811],
	'MN3_LS2': [48,14125],
	'MN4_LS1': [101,31075],
	'MN4_LS2': [1094,621503],
	'MN5_LS0': [17555,3107515],
	'MN5_LS1': [169001,6991908],
	'MN5_LS2': [jackpot,139838160]
}


# Functions
def printVerbose(string):
	if verbose:
		print(string)

def printVerboseNoNewline(string):
	if verbose:
		print(string, end='')


# Main program
random.seed(time.time() * 1000.0)

print('Type \'q\' to quit')

running = True
while running:
	week = week + 1
	money = round(money, 2)
	printVerbose('Money: ' + str(money))

	response = input('\nWeek number ' + str(week) + '. It costs £' + str(priceOfTicket) + ' per ticket. Please enter the number of tickets you\'d like to buy for this week or press enter to buy 1 ticket: ')

	#if money > 0:
	#	running = False
	if response.strip().lower() == 'q':
		running = False
	else:
		numberOfTickets = 1
		if response.strip().isdigit():
			numberOfTickets = int(response.strip())
			if numberOfTickets > 100000:
				printVerbose('Maximum tickets set at 10000')
				time.sleep(2)
				numberOfTickets = 10000

		totalTicketsPurchased = totalTicketsPurchased + numberOfTickets
		for i in range(0,numberOfTickets):
			winnings = 0
			money = money - priceOfTicket

			randomNumber = random.randint(1, winningsAndOdds['MN5_LS2'][1])

			printVerboseNoNewline('Ticket ' + str(i+1) + ': ')
			if randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN5_LS2'][1]: # MN5_LS2 - Jackpot won!
				winnings = winningsAndOdds['MN5_LS2'][0]
				money = money + winnings
				printVerbose('Winner (MN5_LS2). You won £' + str(winnings) + ' - Jackpot won!')

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN5_LS1'][1]: # MN5_LS1
				winnings = winningsAndOdds['MN5_LS1'][0]
				money = money + winnings
				printVerbose('Winner (MN5_LS1). You won £' + str(winningsAndOdds['MN5_LS1'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN5_LS0'][1]: # MN5_LS0
				winnings = winningsAndOdds['MN5_LS0'][0]
				money = money + winnings
				printVerbose('Winner (MN5_LS0). You won £' + str(winningsAndOdds['MN5_LS0'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN4_LS2'][1]: # MN4_LS2
				winnings = winningsAndOdds['MN4_LS2'][0]
				money = money + winnings
				printVerbose('Winner (MN4_LS2). You won £' + str(winningsAndOdds['MN4_LS2'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN4_LS1'][1]: # MN4_LS1
				winnings = winningsAndOdds['MN4_LS1'][0]
				money = money + winnings
				printVerbose('Winner (MN4_LS1). You won £' + str(winningsAndOdds['MN4_LS1'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN3_LS2'][1]: # MN3_LS2
				winnings = winningsAndOdds['MN3_LS2'][0]
				money = money + winnings
				printVerbose('Winner (MN3_LS2). You won £' + str(winningsAndOdds['MN3_LS2'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN4_LS0'][1]: # MN4_LS0
				winnings = winningsAndOdds['MN4_LS0'][0]
				money = money + winnings
				printVerbose('Winner (MN4_LS0). You won £' + str(winningsAndOdds['MN4_LS0'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN2_LS2'][1]: # MN2_LS2
				winnings = winningsAndOdds['MN2_LS2'][0]
				money = money + winnings
				printVerbose('Winner (MN2_LS2). You won £' + str(winningsAndOdds['MN2_LS2'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN3_LS1'][1]: # MN3_LS1
				winnings = winningsAndOdds['MN3_LS1'][0]
				money = money + winnings
				printVerbose('Winner (MN3_LS1). You won £' + str(winningsAndOdds['MN3_LS1'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN3_LS0'][1]: # MN3_LS0
				winnings = winningsAndOdds['MN3_LS0'][0]
				money = money + winnings
				printVerbose('Winner (MN3_LS0). You won £' + str(winningsAndOdds['MN3_LS0'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN1_LS2'][1]: # MN1_LS2
				winnings = winningsAndOdds['MN1_LS2'][0]
				money = money + winnings
				printVerbose('Winner (MN1_LS2). You won £' + str(winningsAndOdds['MN1_LS2'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN2_LS1'][1]: # MN2_LS1
				winnings = winningsAndOdds['MN2_LS1'][0]
				money = money + winnings
				printVerbose('Winner (MN2_LS1). You won £' + str(winningsAndOdds['MN2_LS1'][0]))

			elif randomNumber <= winningsAndOdds['MN5_LS2'][1]/winningsAndOdds['MN2_LS0'][1]: # MN2_LS0
				winnings = winningsAndOdds['MN2_LS0'][0]
				money = money + winnings
				printVerbose('Winner (MN2_LS0). You won £' + str(winningsAndOdds['MN2_LS0'][0]))

			else:
				printVerbose('Loser!')

			if winnings > bestWinnings:
				bestWinnings = winnings

print('\n\nThe most amount you won on a ticket in ' + str(week-1) + ' weeks after playing ' + str(totalTicketsPurchased) + ' tickets was £' + str(bestWinnings) + '. You have ended the simulation with £' + str(money))
