import sys

morse_code_dict = {
    'A': '.-',     'B': '-...',   'C': '-.-.', 
    'D': '-..',    'E': '.',      'F': '..-.',
    'G': '--.',    'H': '....',   'I': '..',
    'J': '.---',   'K': '-.-',    'L': '.-..',
    'M': '--',     'N': '-.',     'O': '---',
    'P': '.--.',   'Q': '--.-',   'R': '.-.',
    'S': '...',    'T': '-',      'U': '..-',
    'V': '...-',   'W': '.--',    'X': '-..-',
    'Y': '-.--',   'Z': '--..',   
    '0': '-----',  '1': '.----',  '2': '..---',
    '3': '...--',  '4': '....-',  '5': '.....',
    '6': '-....',  '7': '--...',  '8': '---..',
    '9': '----.'
}
def to_morse_code(text):
    morseCode = ''
    for c in text.upper():
        if c in morse_code_dict:
            morseCode += morse_code_dict[c] + ' '
        elif c == ' ':
            morseCode += '/ '
        else :
            return "ERROR" 
    return morseCode

print(to_morse_code(" ".join(sys.argv[1::]))) if len(sys.argv) > 1 else print("invalid arguments!")