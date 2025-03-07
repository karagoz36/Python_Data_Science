# **Python Data Science Bootcamp**

## **Overview**
Welcome to the **Python Data Science Bootcamp**! This repository contains exercises and projects that build essential skills in Python programming, data manipulation, image processing, object-oriented programming, and data-oriented design. The bootcamp is divided into four structured modules:

1. **Module 1 - Python Basics**: Fundamental programming concepts.
2. **Module 2 - NumPy & Image Processing**: Array manipulations and image processing.
3. **Module 3 - Object-Oriented Programming (OOP)**: Understanding OOP principles.
4. **Module 4 - Data-Oriented Design**: Structuring code efficiently for data-centric applications.

## **Project Structure**
Each module consists of multiple exercises stored in separate directories:

```
.
├── module_1/   # Python Basics
├── module_2/   # NumPy & Image Processing
├── module_3/   # Object-Oriented Programming
├── module_4/   # Data-Oriented Design
├── LICENSE
├── README.md
└── pyproject.toml
```

## **Module Breakdown**

### **📌 Module 1 - Python Basics**
- Writing basic scripts and functions.
- Understanding Python data structures (`list`, `tuple`, `set`, `dict`).
- Implementing simple programs with user input and assertions.
- Handling `None`, `NaN`, empty strings, and boolean values.
- Creating a simple **Morse code converter** and a **progress bar**.
- Packaging and installing Python modules.

### **📌 Module 2 - NumPy & Image Processing**
- Working with **NumPy arrays** and **PIL (Pillow)** for image manipulation.
- Implementing **BMI calculations** and **2D array slicing**.
- Loading and visualizing datasets using **Pandas**.
- Extracting image **sections (zooming)** and applying **color filters**.
- Rotating images and converting RGB to grayscale.

### **📌 Module 3 - Object-Oriented Programming (OOP)**
- Learning **class inheritance** and **abstraction**.
- Implementing **Game of Thrones-themed character classes**.
- Understanding **multiple inheritance and method resolution order (MRO)**.
- Performing **vector calculations** using operator overloading.
- Implementing a **dot product calculator** using decorators.

### **📌 Module 4 - Data-Oriented Design**
- Implementing **statistical functions** (mean, median, standard deviation, variance).
- Creating **function wrappers** using decorators.
- Managing function execution limits with **call limit decorators**.
- Using **Python dataclasses** to generate structured data.

## **Coding Standards & Rules**
- **Python Version**: Python 3.10.
- **Allowed Libraries**: Only libraries explicitly mentioned in the exercises.
- **Coding Standards**:
  - All functions must have **docstrings (`__doc__`)**.
  - Code must follow **PEP8 standards (`flake8`)**.
  - No global variables.
  - No **wildcard imports** (e.g., `from pandas import *` is not allowed).
- **Project Submission**:
  - Work must be stored in the assigned **Git repository**.
  - Each module must be turned in separately.
  - Peer evaluations must be completed within **two days**.

## **How to Run the Code**

### **Installation Requirements**
Ensure you have Python 3.10+ installed and required dependencies:
```sh
pip install numpy pandas pillow matplotlib flake8
```

### **Running Exercises**
To execute an exercise, navigate to its directory and run the script:
```sh
python ex00/example_script.py
```
For exercises involving datasets:
```sh
python ex02/load_csv.py dataset.csv
```
For object-oriented exercises:
```sh
python module_3/ex03/vector_calculator.py
```

## **Evaluation & Testing**
- **Testing**: Each exercise includes a test script (`test.py`). Run it to verify your implementation.
```sh
python test.py
```
- **Linting**: Use `flake8` to check code quality.
```sh
flake8
