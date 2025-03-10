import matplotlib.pyplot as plt
from load_csv import load


def main():
    """
    It creates a visualization for a specific country over time
    """

    data = load("life_expectancy_years.csv")
    if data is None:
        print("Error: Could not load the dataset")
        return

    country = "France"

    try:
        if country not in data['country'].values:
            print(f"Error: {country} not found in the dataset")
            return

        country_data = data[data['country'] == country]

        # The first column is 'country', so we exclude it
        years = data.columns[1:].astype(int)
        life_expect = country_data.iloc[0, 1:].values

        plt.figure(figsize=(12, 6))
        plt.plot(years, life_expect, linestyle='-', color='blue', linewidth=2)

        plt.title(f'{country} Life Expectancy Projections', fontsize=15)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Life Expectancy', fontsize=12)

        plt.xticks(range(1800, 2101, 40))

        plt.grid(True, linestyle='--', alpha=0.7)

        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occured: {e}")


if __name__ == "__main__":
    main()
