import matplotlib.pyplot as plt
from load_csv import load
import numpy as np


def convert_population(value):
    """
    Convert population values like '9.76M' to float.

    Args:
        value: A string representing population value

    Returns:
        float: Numeric population value
    """
    try:
        # Already a numeric value
        return float(value)
    except ValueError:
        # Handle values with suffixes like 'M' or 'B'
        if isinstance(value, str):
            value = value.strip()
            if value.endswith('M'):
                return float(value[:-1]) * 1000000
            elif value.endswith('B'):
                return float(value[:-1]) * 1000000000
            elif value.endswith('k') or value.endswith('K'):
                return float(value[:-1]) * 1000
            else:
                return 0  # Return 0 for any other format we don't recognize
        return 0


def main():
    """
    Main function that loads population data and creates
    a visualization comparing population of two countries over time.
    """
    # Load the dataset
    data = load("population_total.csv")

    if data is None:
        print("Error: Could not load the dataset")
        return

    # Select your campus country and another country to compare
    campus_country = "Belgium"  # Replace with your campus country
    comparison_country = "France"  # Replace with a country of your choice

    try:
        # Check if both countries exist in the dataset
        if campus_country not in data['country'].values:
            print(f"Error: {campus_country} not found in the dataset")
            return

        if comparison_country not in data['country'].values:
            print(f"Error: {comparison_country} not found in the dataset")
            return

        # Extract data for the specific countries
        campus_data = data[data['country'] == campus_country].iloc[0, 1:]
        comparison_data = data[data['country'] == comparison_country].iloc[0, 1:]

        # Convert string values to float using our helper function
        campus_pop = [convert_population(val) for val in campus_data]
        comparison_pop = [convert_population(val) for val in comparison_data]

        # Extract years and convert to integers
        years = np.array(data.columns[1:]).astype(int)

        # Filter data for years between 1800 and 2050
        mask = (years >= 1800) & (years <= 2050)
        filtered_years = years[mask]
        filtered_campus_pop = np.array(campus_pop)[mask]
        filtered_comparison_pop = np.array(comparison_pop)[mask]

        # Create the plot
        plt.figure(figsize=(14, 7))

        # Plot both countries with different colors and line styles
        plt.plot(filtered_years, filtered_campus_pop,
                 marker='', linestyle='-', linewidth=2, color='red',
                 label=f'{campus_country}')

        plt.plot(filtered_years, filtered_comparison_pop,
                 marker='', linestyle='--', linewidth=2, color='blue',
                 label=f'{comparison_country}')

        # Add title and labels
        plt.title(f'Population Comparison: {campus_country} vs {comparison_country} (1800-2050)',
                  fontsize=15)
        plt.xlabel('Year', fontsize=12)
        plt.ylabel('Population', fontsize=12)

        # Format y-axis with commas for thousands
        plt.gca().get_yaxis().set_major_formatter(
            plt.matplotlib.ticker.FuncFormatter(lambda x, p: format(int(x), ','))
        )

        # Add legend
        plt.legend(fontsize=12)

        # Add grid for better readability
        plt.grid(True, linestyle='--', alpha=0.7)

        # Improve the x-axis ticks (show fewer years for readability)
        plt.xticks(range(1800, 2051, 25), rotation=45)

        # Show the plot
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
