import pandas as pd
import matplotlib.pyplot as plt
from load_csv import load  # Önceki egzersizde yazdığımız load fonksiyonunu kullanıyoruz.

def compare_population(country1: str, country2: str):
    """
    Loads population data and compares two countries' population trends from 1800 to 2050.

    :param country1: str - First country to compare.
    :param country2: str - Second country to compare.
    """
    # CSV dosyasını yükle
    df = load("population_total.csv")

    if df is None:
        return

    # Ülkelerin veri setinde olup olmadığını kontrol et
    if country1 not in df['country'].values or country2 not in df['country'].values:
        print(f"Error: One or both of the countries ({country1}, {country2}) not found in dataset.")
        return

    # İlgili ülkelerin verilerini al
    country1_data = df[df['country'] == country1]
    country2_data = df[df['country'] == country2]

    # Yılları seç (ilk sütun 'country' olduğu için onu çıkarıyoruz)
    years = df.columns[1:].astype(int)  # Sütun isimlerini integer'a çeviriyoruz
    values1 = country1_data.iloc[0, 1:].values  # country1 için nüfus verileri
    values2 = country2_data.iloc[0, 1:].values  # country2 için nüfus verileri

    # Grafiği çiz
    plt.figure(figsize=(10, 5))
    plt.plot(years, values1, marker='o', linestyle='-', color='b', label=country1)
    plt.plot(years, values2, marker='s', linestyle='--', color='r', label=country2)

    # Grafik detayları
    plt.xlabel("Year")
    plt.ylabel("Total Population")
    plt.title(f"Population Comparison: {country1} vs {country2}")
    plt.legend()
    plt.grid(True)

    # Grafiği göster
    plt.show()

if __name__ == "__main__":
    compare_population("France", "Belgium")  # Örnek olarak Fransa ve Türkiye'yi karşılaştırıyoruz.
