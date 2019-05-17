from tkinter import *
import tkinter.font
from gpiozero import LED
import RPi.GPIO
import time

RPi.GPIO.setmode(RPi.GPIO.BCM)

### HARDWARE DEFINITIONS ###
led=LED(14)


### GUI DEFINITIONS ###
win = Tk()
win.title("Morse Code")
myFont = tkinter.font.Font(family = 'Helvetica', size = 12, weight = "bold")

MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-'} 

def encrypt(message): 
    cipher = '' 
    for letter in message.upper(): 
        if letter != ' ': 
  
            # Looks up the dictionary and adds the 
            # correspponding morse code 
            # along with a space to separate 
            # morse codes for different characters 
            cipher += MORSE_CODE_DICT[letter] + ' '
        else: 
            # 1 space indicates different characters 
            # and 2 indicates different words 
            cipher += ' '
  
    return cipher

def blink():
    for symbol in encrypt(T.get()):
        if symbol == " ":
            time.sleep(1)
        if symbol == ".":
            led.on()
            time.sleep(0.5)
            led.off()
            time.sleep(1)
        if symbol == "-":
            led.on()
            time.sleep(2)
            led.off()
            time.sleep(1)

def close():
    RPi.GPIO.cleanup()
    win.destroy()



### WIDGETS ###

# Button, triggers the connected command when it is pressed
T = Entry(win, width=12)
T.grid(row=1, column=1)

submit = Button(win, text='Submit', font=myFont, command=blink, bg='bisque2', height=1, width=3)
submit.grid(row=1, column=2)

exitButton = Button(win, text='Exit', font=myFont, command=close, bg='red', height=1, width=6)
exitButton.grid(row=2, column=1)

win.protocol("WM_DELETE_WINDOW", close) # cleanup GPIO when user closes window

win.mainloop() # Loops forever