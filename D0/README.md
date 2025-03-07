# **Python Data Science Bootcamp - Module 1**

## **Overview**
This repository contains the solutions for the first module of the **Python Data Science Bootcamp**. The exercises focus on mastering the **fundamentals of Python**, including basic scripting, functions, packages, progress bars, and even creating a Python package.

## **Structure**
Each exercise is located in a separate directory (`exXX/`), and follows the given instructions:

```
.
├── ex00/   # First Python script
├── ex01/   # First use of a package
├── ex02/   # First function in Python
├── ex03/   # NULL not found
├── ex04/   # The Even and the Odd
├── ex05/   # First standalone program
├── ex06/   # Recreating the filter function
├── ex07/   # Morse code conversion
├── ex08/   # Implementing a progress bar
├── ex09/   # Creating a Python package
├── LICENSE
├── README.md
└── pyproject.toml
```

## **Exercises Breakdown**
### **🚀 ex00 - First Python Script**
- Modify Python data structures (`list`, `tuple`, `set`, `dict`).
- Display formatted elements as per given requirements.

### **📦 ex01 - First Use of a Package**
- Work with the `time` and `datetime` libraries.
- Format and display timestamps correctly.

### **🔍 ex02 - First Function in Python**
- Implement a function that prints object types.
- Ensure the function returns a fixed value.

### **❌ ex03 - NULL Not Found**
- Identify and handle `None`, `NaN`, `0`, empty strings, and `False` values.

### **🔢 ex04 - The Even and the Odd**
- Create a script to determine if a number is **even** or **odd**.
- Handle invalid inputs with assertions.

### **📝 ex05 - First Standalone Program**
- Build a program that **analyzes a given text**.
- Count uppercase/lowercase letters, spaces, punctuation, and digits.

### **🔍 ex06 - Recreating `filter()`**
- Implement a custom version of Python’s built-in `filter()`.
- Create a script that filters words based on their length.

### **💬 ex07 - Morse Code Conversion**
- Convert a given string to **Morse Code**.
- Handle errors and support space-separated Morse output.

### **⏳ ex08 - Implementing a Progress Bar**
- Recreate the **`tqdm` progress bar** using `yield` and `sys.stdout`.
- Compare the custom implementation with the original.

### **📦 ex09 - Creating a Python Package**
- Package a custom module (`ft_package`) and make it installable via `pip`.
- The package should be listed in `pip list` and display information when `pip show ft_package` is used.

## **Submission Rules**
- **Python Version**: `Python 3.10` must be used.
- **Allowed Libraries**: Only libraries explicitly mentioned in the exercise instructions can be used.
- **Coding Standards**: Code must pass `flake8` (`pip install flake8`).
- **Project Structure**:
  - Each exercise must be in its respective `exXX/` directory.
  - The repository must contain **only** the required files:
    ```
    Files to turn in: *.py, *.txt, *.toml, README.md, LICENSE
    ```
  - No global variables are allowed.
  - Every function must have proper documentation (`__doc__`).

## **How to Build and Install `ex09` Package**
To package and install **`ft_package`** from `ex09/`:
```bash
# Install build tools
pip install build

# Build the package
python -m build

# Install the package
pip install ./dist/ft_package-0.0.1.tar.gz

# Verify installation
pip show ft_package
```

## **Testing**
Run the test scripts included in each directory:
```bash
python test.py
```
For example, to test `ex09`:
```bash
python test.py
```
Expected output:
```
2
0
```
