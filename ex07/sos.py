# sos.py

import sys

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
    '9': '----.', ' ': '/'
}


def text_to_morse(text: str) -> str:
    """
    Converts a givent text into Morse code.
    """

    try:
        text = text.upper()

        if any(char not in MORSE_DICT for char in text):
            raise AssertionError("the arguments are bad")
        # for char in text:
        # if char not in MORSE_DICT:
        #     raise AssertionError("the arguments are bad")
        morse_code = ' '.join(MORSE_DICT[char] for char in text)
        return morse_code

    except AssertionError as e:
        print(f"AssertionError: {e}")
        sys.exit(1)


def main():
    """
    Handles input validation and calls text_to_morse function.
    """
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        print(text_to_morse(text))

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
