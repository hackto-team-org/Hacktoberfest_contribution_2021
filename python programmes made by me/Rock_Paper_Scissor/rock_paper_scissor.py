# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 00:31:15 2020

@author: admin
"""
import utils
import time 
import random
from colorama import Style, Fore

print(''' 
   ___           __       ___                        ____    _                    
  / _ \___  ____/ /__    / _ \___ ____  ___ ____    / __/___(_)__ ___ ___  _______
 / , _/ _ \/ __/  '_/   / ___/ _ `/ _ \/ -_) __/   _\ \/ __/ (_-<(_-</ _ \/ __(_-<
/_/|_|\___/\__/_/\_( ) /_/   \_,_/ .__/\__/_/ ( ) /___/\__/_/___/___/\___/_/ /___/
                   |/           /_/           |/             by @Sam-Ny
''')


print(Style.BRIGHT + Fore.GREEN + '[*] ' + Style.RESET_ALL + 'Starting the Rock Paper Scissors game!')
time.sleep(2)
print('')
player_name = input(Style.BRIGHT + 'Please enter your name > ' + Style.RESET_ALL)
time.sleep(1)
print('')
print(Style.BRIGHT + Fore.GREEN + '[*] ' + Style.RESET_ALL + 'Pick a hand: (0: Rock, 1: Paper, 2: Scissors)')
time.sleep(1)
print('')
player_hand = int(input(Style.BRIGHT + 'Please enter a number (0-2) > ' + Style.RESET_ALL))

if utils.validate(player_hand):
    # Assign a random number between 0 and 2 to computer_hand using randint
    computer_hand =random.randint(0,2) 
    
    print('')
    print('----------------------------------------------------------')
    utils.print_hand(player_hand, player_name)
    utils.print_hand(computer_hand, 'Computer')

    result = utils.judge(player_hand, computer_hand)
    print(Style.BRIGHT + Fore.YELLOW + '[Result] ' + Style.RESET_ALL + result)
    print('----------------------------------------------------------')
else:
    print(Style.BRIGHT + Fore.RED + '[-] ' + Style.RESET_ALL + 'Please enter a valid number')
