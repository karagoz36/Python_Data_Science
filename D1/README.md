# Python Data Science Bootcamp - Module 2

## 📀 Module Overview
This module focuses on **image processing and NumPy array manipulations** in Python.  
We work with image files, manipulate their pixel values, and apply various operations like slicing, filtering, and transformations.

### ✅ Key Learning Points
- Loading and processing images using **PIL (Pillow)**
- Manipulating images as **NumPy arrays**
- **Slicing & Zooming** on images
- **Grayscale & Color Filtering**
- **Image Rotation & Transposition**
- **Visualizing images using Matplotlib**

---

## 📀 Exercises

### 1️⃣ Exercise 00: Give my BMI
📀 **Objective:** Implement a function to calculate the **BMI (Body Mass Index)** using lists of height and weight values.  
🔹 **Key Concepts:** Lists, NumPy, Error Handling  

✅ **Functions:**
```python
def give_bmi(height: List[Union[int, float]], weight: List[Union[int, float]]) -> List[float]
def apply_limit(bmi: List[Union[int, float]], limit: int) -> List[bool]
```
✅ **Key Features:**
- Calculates **BMI** using the formula `weight / (height^2)`.
- Handles **input validation** (ensures values are numeric and lists have the same length).
- Applies a threshold to check if BMI is above a certain limit.

---

### 2️⃣ Exercise 01: 2D Array
📀 **Objective:** Implement a function to **slice a 2D array** and return a smaller section.  
🔹 **Key Concepts:** NumPy slicing, shape properties, error handling.  

✅ **Function:**
```python
def slice_me(family: List[List[float]], start: int, end: int) -> List[List[float]]
```
✅ **Key Features:**
- Takes a **2D list (matrix)** and slices it based on provided indices.
- Prints the **shape before and after slicing**.
- **Handles errors** if the input is not a valid 2D list.

---

### 3️⃣ Exercise 02: Load My Image
📀 **Objective:** Implement a function to **load an image** and return its NumPy representation.  
🔹 **Key Concepts:** Image processing, NumPy arrays, PIL (Pillow).  

✅ **Function:**
```python
def ft_load(path: str) -> np.ndarray
```
✅ **Key Features:**
- Loads an image from a file path.
- Converts it into a **NumPy array**.
- Prints the **image shape** (height, width, channels).
- Handles **file errors** if the image is missing or in an unsupported format.

---

### 4️⃣ Exercise 03: Zoom on Me
📀 **Objective:** Extract a **zoomed-in region** from an image.  
🔹 **Key Concepts:** NumPy slicing, zooming, image manipulation.  

✅ **Functions:**
```python
def zoom_image(image_array: np.ndarray, start_x: int, start_y: int, size: int) -> np.ndarray
```
✅ **Key Features:**
- Takes an image as a **NumPy array**.
- Extracts a **square section** of `size x size` from the given `start_x, start_y`.
- Displays both the **original and zoomed images**.

✅ **This exercise depends on:**  
- `load_image.py` → Used for image loading.

---

### 5️⃣ Exercise 04: Rotate Me
📀 **Objective:** Extract a central region from an image and **rotate it (transpose)**.  
🔹 **Key Concepts:** Image transposition, slicing, NumPy manipulations.  

✅ **Functions:**
```python
def crop_center(image_array: np.ndarray, size: int) -> np.ndarray
def rotate_image(image_array: np.ndarray) -> np.ndarray
```
✅ **Key Features:**
- Extracts a **centered square** from an image.
- Uses **`np.transpose()`** to **rotate** the extracted region.
- Displays **original, cropped, and rotated** versions.

✅ **This exercise depends on:**  
- `load_image.py` → Used for image loading.

---

### 6️⃣ Exercise 05: Pimp My Image
📀 **Objective:** Apply **color transformations and filters** to an image.  
🔹 **Key Concepts:** NumPy operations, color channel manipulation, grayscale conversion.  

✅ **Functions:**
```python
def ft_invert(image_array: np.ndarray) -> np.ndarray
def ft_red(image_array: np.ndarray) -> np.ndarray
def ft_green(image_array: np.ndarray) -> np.ndarray
def ft_blue(image_array: np.ndarray) -> np.ndarray
def ft_grey(image_array: np.ndarray) -> np.ndarray
```
✅ **Key Features:**
- **Inverts colors** (negative image).
- Extracts **only red, green, or blue** channels.
- Converts **RGB to grayscale**.
- Displays all transformations in a **grid layout using Matplotlib**.

✅ **This exercise depends on:**  
- `load_image.py` → Used for image loading.

---

## 📀 How to Run the Code
Make sure you have **Python 3.10+** installed and the following dependencies:

```sh
pip install numpy pillow matplotlib flake8
```

### **Run Each Exercise**
```sh
python ex00/give_bmi.py
python ex01/array2D.py
python ex02/load_image.py
python ex03/zoom.py
python ex04/rotate.py
python ex05/pimp_image.py
```

---

## 📀 Notes
✅ **Code follows PEP8 standards** (`flake8` compatible).  
✅ **Matplotlib is used for visualizing images.**  
✅ **Exercises build upon previous ones, enhancing reusability.**  
✅ **Exercises 03, 04, and 05 depend on `load_image.py` for image loading.**  

---

🚀 **This module provides a strong foundation in image processing using NumPy & Matplotlib!**  
