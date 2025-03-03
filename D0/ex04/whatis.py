#whatis.py

import sys

def main():
	try:

		if len(sys.argv) == 1:
			return
		if len(sys.argv) > 2:
			raise AssertionError("more than one argument is provided")

		num = int(sys.argv[1])

		if num % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")

	except AssertionError as e:
		print(f"AssertionError: {e}") # Print the error message without traceback
	except ValueError:
		print("AssertionError: argument is not an integer") # Handle invalid integer input

if __name__ == "__main__":
	main()
