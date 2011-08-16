# A countdown for the Pomodoro Clock.
# Works for 25 minutes.
# Original source: http://www.gidforums.com/t-9240.html Thanks.

from time import time
from time import sleep
from re import sub
from os import system
from os import name

def clear():
    system('cls' if name == 'nt' else 'clear')

def countdown(tiempo):
    start = time()
    lastprinted = 0
    finish = start + tiempo
    
    while time() < finish:
        now = int(time())
        if now != lastprinted:
            cuenta = int(finish - now)
            if cuenta >= 60:
                mins = int(cuenta/60)
                rsecs = cuenta % 60
                hora = str("%.2f" % (mins + rsecs / 100.0))
                hora_real = sub('\.',':',hora)
                clear()
                print hora_real
            else:
                clear()
                print cuenta
            lastprinted = now
        sleep(0.5)
