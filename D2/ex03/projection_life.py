#!/usr/bin/env python3
"""
Program shows corelation between life expect and GDP per capita for chosen year
"""
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load


def format_pop(value, pos):
    if value >= 1e3 and value <= 1e6:
        return f"{value/1e3:.0f}k"
    else:
        return f"{int(value)}"


def main():
    """"
    Loads two CSV files and creates a scatter plot showing correlation
    """
    path_to_GDP = "income_per_person_gdppercapita_ppp_inflation_adjusted.csv"
    income_data = load(path_to_GDP)
    life_exp_data = load("life_expectancy_years.csv")

    if income_data is None or life_exp_data is None:
        print("Error: Could not load Datasets.")
        return

    target_year = '1900'

    # country name and the target year
    # Using double "[[]]"" to ensure we get a DataFrame, not a Series
    income = income_data[['country', target_year]].copy()
    life_exp = life_exp_data[['country', target_year]].copy()

    income = income.rename(columns={target_year: 'income'})
    life_exp = life_exp.rename(columns={target_year: 'life_expectancy'})

    merged_data = income.merge(life_exp, on='country')

    plt.figure(figsize=(8, 6))
    plt.scatter(merged_data['income'], merged_data['life_expectancy'],
                alpha=0.7)

    plt.title(f'{target_year}')
    plt.xlabel('Gross Domestic Product')
    plt.ylabel('Life Expectancy')

    # Use logarithmic scale for x-axis
    # It helps to visualize countries with vastly different income levels
    plt.xscale('log')

    # It customize x axis values to accomplish instructions
    custom_ticks = [300, 1000, 10000]
    plt.xticks(custom_ticks)

    # Converts thousands to k
    plt.gca().xaxis.set_major_formatter(ticker.FuncFormatter(format_pop))

    correlation = merged_data['income'].corr(merged_data['life_expectancy'])
    plt.annotate(f'Correlation: {correlation:.2f}',
                 xy=(0.05, 0.95), xycoords='axes fraction')

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
