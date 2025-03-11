import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from load_csv import load
import numpy as np


def format_pop(value, pos):
    """
    Format back population values with K, M, B
    """
    if value >= 1e9:
        return f"{value/1e9:.0f}B"
    elif value >= 1e6:
        return f"{value/1e6:.0f}M"
    elif value >= 1e3:
        return f"{value/1e3:.0f}K"
    else:
        return f"{value:.0f}"


def convert_pop(value):
    """
    Convert population values like '9.76M' to float.
    """
    try:
        return float(value)
    except ValueError:
        if isinstance(value, str):
            value = value.strip()
            if value.endswith('M'):
                return float(value[:-1]) * 1e6
            if value.endswith('B'):
                return float(value[:-1]) * 1e9
            elif value.endswith('k') or value.endswith('K'):
                return float(value[:-1]) * 1e3
            else:
                return 0


def main():
    """
    This func. creates a visualization comparing population
    """
    data = load("population_total.csv")

    if data is None:
        print("Error: Could not load the dataset")
        return

    A_country = "Belgium"
    B_country = "France"

    try:
        if A_country not in data['country'].values:
            print(f"Error: {A_country} not found in the dataset")
            return

        if B_country not in data['country'].values:
            print(f"Error: {B_country} not found int the dataset")
            return

        A_data = data[data['country'] == A_country].iloc[0, 1:]
        B_data = data[data['country'] == B_country].iloc[0, 1:]

        A_pop = [convert_pop(val) for val in A_data]
        B_pop = [convert_pop(val) for val in B_data]

        years = np.array(data.columns[1:]).astype(int)

        mask = (years >= 1800) & (years <= 2050)
        flt_years = years[mask]
        flt_A_pop = np.array(A_pop)[mask]
        flt_B_pop = np.array(B_pop)[mask]

        plt.figure(figsize=(14, 7))

        plt.plot(flt_years, flt_A_pop, linestyle='-',
                 linewidth=2, color='blue', label=f'{A_country}')

        plt.plot(flt_years, flt_B_pop, linestyle='-',
                 linewidth=2, color='green', label=f'{B_country}')

        plt.title(f'Population Projections: {A_country} vs {B_country}')
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Population', fontsize=12)

        plt.gca().yaxis.set_major_locator(ticker.MaxNLocator(4))
        plt.gca().get_yaxis().set_major_formatter(
            ticker.FuncFormatter(format_pop)
            )

        plt.legend(fontsize=12, loc='lower right')

        plt.grid(True, linestyle='--', alpha=0.7)

        plt.xticks(range(1800, 2051, 40))

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
