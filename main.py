#-----------------------------This is Portfolio Project 1 of 100 Days of Code on Udemy ---------------------------#
#----------------------------- Created on 2/8/2022 by Gavra J Buckman --------------------------------------------#
# Requirement is to create a command line program that will convert text into Morse code characters.

#----------------------------------- IMPORT STATEMENTS ------------------------------------------------------------#
import re

#------------------------------------ CONSTANTS -------------------------------------------------------------------#
MORSE_CODE_DICT = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
    'i': '..',
    'j': '.---',
    'k': '-.-',
    'l': '.-..',
    'm': '--',
    'n': '-.',
    'o': '---',
    'p': '.--.',
    'q': '--.-',
    'r': '.-.',
    's': '...',
    't': '-',
    'u': '..-',
    'v': '...-',
    'w': '.--',
    'x': '-..-',
    'y': '-.--',
    'z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-...',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': '  '
}
#------------------------------------ FUNCTIONS -------------------------------------------------------------------#
def convert_text_to_morse(text):
    """" This function takes a string input and converts it character by character into morse code.
    Returns a string with the morse code output"""

    # Remove special characters
    new_text = re.sub('[^A-Za-z0-9 ]+', '', text)
    #print(new_text)

    # List comprehension to create a new list of the text in morse code
    morse_text_list = [MORSE_CODE_DICT[char] for char in new_text]

    # Convert to a string and return it. Make sure there is a space between letters and 3 spaces between words.
    return ' '.join(morse_text_list)

#------------------------------------ UI SETUP -------------------------------------------------------------------#
# Ask user to input a string to be converted
user_input = input("Please enter a string to be converted into morse code: \n").lower()
morse_text = convert_text_to_morse(user_input)
print(morse_text)