import sys
import string


def count_chars(text: str):
    """
    Counts different character types in a given text.
    """
    total_chars = len(text)
    upper = sum(1 for c in text if c.isupper())
    lower = sum(1 for c in text if c.islower())
    punct = sum(1 for c in text if c in string.punctuation)
    spaces = sum(1 for c in text if c.isspace())
    digits = sum(1 for c in text if c.isdigit())
    print(f"The text contains {total_chars} characters:")
    print(f"{upper} upper letters")
    print(f"{lower} lower letters")
    print(f"{punct} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


def main():
    """
    Handles user input and argument validation.
    """
    try:
        if len(sys.argv) == 1:
            text = input("What is the text to count?\n")
        elif len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            text = sys.argv[1]

        count_chars(text)
        # print(count_chars.__doc__)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
