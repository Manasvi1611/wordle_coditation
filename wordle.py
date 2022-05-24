"""--------------Doc String---------------------
Before running the file run the following commands : 
pip install wget
pip install colorama
"""

from colorama import Fore,Style # For prettifying the output
import random
import wget
import os
from os.path import exists as file_exists

URL = "https://raw.githubusercontent.com/charlesreid1/five-letter-words/master/sgb-words.txt"
if(file_exists('word_list.txt')):
    print('File exists')
    os.remove('word_list.txt')  # Removing the file if it already exists
else:
    print('File doesn\'t exist')
# Downloading the word list and saving it to word_list.txt
wget.download(URL, "word_list.txt")
play = 1
streak = 0
total_plays = 0
wins = 0
max_streak = 0
prev_play =-1 #0 for loss , 1 for win

def print_dict(dict):
    s= ""
    for key,value in dict.items():
        s+=f"{key} : {value}\n"
    return s
while(play):  # Loop until user wishes to quit

    # Reading lines from a file
    word_file = open('word_list.txt', 'r')
    word_list = word_file.readlines()
    word = word_list[random.randint(0, len(word_list))]

  

    won = 0  # This is a flag
    total_plays += 1
    win_percent = (wins/total_plays)*100.0
    for i in range(0, 6):
        res = []

        if(i > 4 and won == 0):
            prev_play=0
            max_streak = max(max_streak,streak)
            streak=0
            print('Sorry you lost ! ')
            print(f'{Fore.LIGHTYELLOW_EX} The word was {word} {Style.RESET_ALL}')
            stats ={'Total Plays': total_plays, 'Win Percentage': (
                wins/total_plays)*100, 'Max Streak': max_streak,'Current Streak':streak}
            print(f"{Fore.LIGHTCYAN_EX}Stats are :\n"+print_dict(stats)+f"{Style.RESET_ALL}")
            play = int(
                input(' Wanna play again ? \nPress 1 to continue, 0 to quit\n'))
            break
        if(won != 0):
            if(prev_play!=0):
                streak+=1
            max_streak = max(max_streak,streak)
            prev_play=1
            wins += 1
            print(f'{Fore.GREEN}You won !{Style.RESET_ALL}')
            stats = {'Total Plays': total_plays, 'Win Percentage': (
                wins/total_plays)*100, 'Max Streak': max_streak,'Current Streak': streak}
            print(f"{Fore.LIGHTCYAN_EX}Stats are :\n"+print_dict(stats)+f"{Style.RESET_ALL}")
            play = int(input(
                f'{Fore.LIGHTMAGENTA_EX} Wanna play again ? \nPress 1 to continue, 0 to quit{Style.RESET_ALL}\n'))
            break
        print("Chance "+str(i+1))
        flag = 1
        while(flag):
            w = input('Enter the word : ')
            if(w == word):
                flag = 0
                won = 1
            elif(w != word):
                count = 0
                for ind in range(0, len(w)):

                    if(w[ind] == word[ind]):
                        count += 1
                        res.append(f"{Fore.GREEN}{w[ind]}{Style.RESET_ALL}")
                        if(count == 5):
                            won = 1
                    elif(w[ind] in word):
                        res.append(f"{Fore.YELLOW}{w[ind]}{Style.RESET_ALL}")
                    else:
                        res.append(
                            f"{Fore.LIGHTBLACK_EX}{w[ind]}{Style.RESET_ALL}")
                print("".join(res))
                flag = 0
