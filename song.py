import sys
from time import sleep
import time
from colorama import Fore


def song():
    words = [('When you asked me for sum more,', 0.05),
             ('I was energized', 0.05),
             ('Couldnt see your eyes,', 0.08),
             ('they were up inside', 0.09),
             ('When you asked if I could see,', 0.05),
             ('I was pulverised', 0.07),
             ('Sat in overdrive,', 0.1),
             ('test & recognise', 0.09)
             ]

    delays = [0.5, 0.6, 0.3, 0.6, 0.4, 0.3, 0.6, 0.6]

    for i, (word, char_delay) in enumerate(words):
        for char in word:
            print(Fore.CYAN + char, end='')
            sys.stdout.flush()
            sleep(char_delay)
        time.sleep(delays[i])
        print('')


song()
