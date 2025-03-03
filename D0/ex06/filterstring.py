# filterstring.py

import sys
from ft_filter import ft_filter


def main():
    """
    Filters words from a given string based on a specified length.
    thanks to akka et fatta
    """
    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")

        text = sys.argv[1]
        try:
            min_len = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
        words = text.split()
        filtered = list(ft_filter(lambda word: len(word) > min_len, words))
        print(filtered)

    except AssertionError as e:
        print(f"AssertionError: {e}")


if __name__ == "__main__":
    main()
