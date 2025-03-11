# 💪 Python Data Science Bootcamp - Module 2: Data Table

This module focuses on **loading, manipulating, and visualizing tabular data** using Python libraries such as `pandas`, `matplotlib`, and `seaborn`.

---

## 📚 Key Learning Points

- **Reading and handling CSV files** with `pandas`
- **Filtering and merging datasets**
- **Creating visualizations** with `matplotlib` and `seaborn`
- **Applying transformations and cleaning data**
- **Using logarithmic scales and formatters** for better visualization

---

## 📂 Project Structure

```
.
├── ex00/               # Load CSV dataset
│   ├── load_csv.py
│
├── ex01/               # Visualizing Life Expectancy Over Time
│   ├── aff_life.py
│
├── ex02/               # Comparing Country Populations
│   ├── aff_pop.py
│
├── ex03/               # Life Expectancy vs GDP Visualization
│   ├── projection_life.py
│
├── data/               # CSV files
│   ├── life_expectancy_years.csv
│   ├── income_per_person_gdppercapita_ppp_inflation_adjusted.csv
│   ├── population_total.csv
│
├── README.md           # This file
└── requirements.txt    # Python dependencies
```

---

## 🗍 Exercises Breakdown

### **1️⃣ Exercise 00: Load My Dataset**
👉 **Goal:** Implement a function to load a dataset from a CSV file and print its dimensions.
📊 **Concepts:** `pandas.read_csv()`, `.shape`, error handling.

**Example Output:**
```
Loading dataset of dimensions (195, 302)
```

---

### **2️⃣ Exercise 01: Draw My Country**
👉 **Goal:** Create a **line plot** showing **life expectancy** over time for a country.
📊 **Concepts:** Data filtering, `plt.plot()`, adding a **legend**.

**Graph Output:** A line plot of life expectancy trends.

---

### **3️⃣ Exercise 02: Compare My Country**
👉 **Goal:** Compare the **total population** of two countries over time.
📊 **Concepts:** `pd.merge()`, multiple `plt.plot()`, **grid & labels**.

**Graph Output:** Two **population trend lines** on the same plot.

---

### **4️⃣ Exercise 03: Draw My Year**
👉 **Goal:** Analyze the **correlation** between life expectancy and GDP per capita for a given year.
📊 **Concepts:** **Scatter plots**, `log` scale, `seaborn`, `FuncFormatter` to format numbers (`1k` instead of `10³`).

**Graph Output:** A **scatter plot** where each point represents a country.

---

## 🚀 How to Run

1️⃣ **Clone the repository:**
```sh
git clone https://github.com/karagoz36/Python_Data_Science.git
cd python-data-science-module2
```

2️⃣ **Install dependencies:**
```sh
pip install -r requirements.txt
```

3️⃣ **Run an exercise (example for ex03):**
```sh
python ex03/projection_life.py
```

---

## 📦 Dependencies

- Python 3.10+
- `pandas`
- `matplotlib`
- `seaborn`

---

## 🏆 Summary

💪 **Loaded, cleaned, and manipulated tabular data using Pandas**
📊 **Created visualizations with Matplotlib & Seaborn**
📊 **Explored trends in life expectancy, population growth, and GDP**
📝 **Learned data transformation and formatting for better readability**
