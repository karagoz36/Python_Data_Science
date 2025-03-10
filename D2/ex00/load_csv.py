import pandas as pd


def load(path: str):
    """
    Loads a dataset from the given path and prints its dimensions.
    """
    try:
        dataset = pd.read_csv(path)
        print(f"Loading dataset of dimensions {dataset.shape}")

        return dataset

    except FileNotFoundError:
        print(f"Error: File '{path}' not found")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{path}' is empty")
        return None
    except pd.erros.ParserError:
        print(f"Error: File '{path}' is not a valid CSV file")
        return None
    except Exception as e:
        print(f"Error loading file: {e}")
        return None


if __name__ == "__main__":
    df = load("life_expectancy_years.csv")
    if df is not None:
        print(df.head())
