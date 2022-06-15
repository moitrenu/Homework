def decode_morse(text: str) -> str:
    morse: dict = {
            'A': '.-',
           'B': '-...',
           'C': '-.-.',
           'D': '-..',
           'E': '.',
           'F': '..-.',
           'G': '--.',
           'H': '....',
           'I': '..',
           'J': '.---',
           'K': '-.-',
           'L': '.-..',
           'M': '--',
           'N': '-.',
           'O': '---',
           'P': '.--.',
           'Q': '--.-',
           'R': '.-.',
           'S': '...',
           'T': '-',
           'U': '..-',
           'V': '...-',
           'W': '.--',
           'X': '-..-',
           'Y': '-.--',
           'Z': '--..',
           '0': '-----',
           '1': '.----',
           '2': '..---',
           '3': '...--',
           '4': '....-',
           '5': '.....',
           '6': '-....',
           '7': '--...',
           '8': '---..',
           '9': '----.',
           ' ': ' ',
    }
    decode_text: str = ''
    for symbol in text.upper():
        if symbol in morse:
            decode_text += f'{morse[symbol]}   '
    return decode_text

def encode_morse(decode_text: str) -> str:
    morse: dict = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.',
        ' ': ' ',
    }
    encode_text: str = ''
    decode_text = decode_text.replace('       ', '   |   ')
    for symbol in decode_text.split('   '):
        if symbol == '|':
            encode_text += ' '
        else:
          for key, val in morse.items():
              if symbol == val:
                  encode_text += key
                  break
    return encode_text
