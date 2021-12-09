# Program that turns a text file entered by the user into an audio and plays it.

from utilities import *
from pyttsx3 import *
from time import sleep
from os import system

try:
    text_file = open('text_file.txt', 'r')
    text_file.close()
except FileNotFoundError:
    text_file = open('text_file.txt', 'w+')
    text_file.close()

while True:
    headline('TEXT READER IN AUDIO')

    digited_text = input('Please, enter the text you want to hear: \n')

    write_text_file(digited_text, text_file)

    text_file = open('text_file.txt', 'r')
    for l in text_file:
        listen_file = l
    text_file.close()

    audio_read(listen_file)
    
    option = input('Continue? [Y/N]').strip().upper()[0]
    if option == 'N':
        break
    system('cls')
    
print()
print('Closing program...')
sleep(1)
print()