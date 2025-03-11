import matplotlib.pyplot as plt
from load_csv import load  # CSV dosyalarını yüklemek için kullanılan özel fonksiyon
import numpy as np

def convert_income(value):
    """
    Gelir değerlerini float türüne çevirir, özel formatları (k, M) destekler.
    
    Args:
        value: Gelir değeri (string veya sayı türünde olabilir)
    
    Returns:
        float: Sayısal gelir değeri
    """
    try:
        return float(value)  # Eğer zaten sayısal bir değer ise direkt dönüştür.
    except ValueError:
        if isinstance(value, str):
            value = value.strip()  # Boşlukları temizle
            if 'k' in value.lower():
                return float(value.lower().replace('k', '')) * 1000  # 'k' = bin
            elif 'M' in value:
                return float(value.replace('M', '')) * 1000000  # 'M' = milyon
            else:
                try:
                    return float(value)  # Eğer başka bir formatta sayıya çevrilebiliyorsa
                except:
                    return 0  # Geçersiz değerler için sıfır döndür
        return 0  # Sayıya çevrilemiyorsa 0 döndür

def main():
    """
    Ana fonksiyon: Veriyi yükler, işler ve grafiği oluşturur.
    """
    # CSV dosyalarını yükle
    life_expectancy = load("life_expectancy_years.csv")
    income = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")
    
    # Dosyalar yüklenemediyse hata mesajı ver
    if life_expectancy is None or income is None:
        print("Error: Could not load one or both datasets")
        return
    
    # 1900 yılı verileri dosyalarda yoksa çık
    if '1900' not in life_expectancy.columns or '1900' not in income.columns:
        print("Error: Year 1900 not found in the datasets")
        return
    
    # 1900 yılına ait yaşam süresi, gelir ve ülkeleri al
    life_data = life_expectancy['1900']
    income_data = income['1900']
    countries = life_expectancy['country']
    
    # Geçerli verileri saklamak için listeler oluştur
    valid_life = []
    valid_income = []
    valid_countries = []
    
    # Verileri temizle ve sayıya çevir
    for i in range(len(countries)):
        try:
            life_value = float(life_data[i])
            income_value = convert_income(income_data[i])
            
            # 0'dan büyük değerler eklenir
            if life_value > 0 and income_value > 0:
                valid_life.append(life_value)
                valid_income.append(income_value)
                valid_countries.append(countries[i])
        except (ValueError, TypeError):
            continue  # Hatalı verileri atla
    
    # Grafik oluşturma
    plt.figure(figsize=(12, 8))
    
    scatter = plt.scatter(
        valid_income, 
        valid_life, 
        alpha=0.7,  # Şeffaflık seviyesi
        s=50,  # Nokta boyutu
        c=range(len(valid_income)),  # Renkleri belirle
        cmap='viridis'  # Renk haritası
    )
    
    # Grafik başlıkları ve etiketleri ekle
    plt.title('Life Expectancy vs. GDP per Capita (1900)', fontsize=15)
    plt.xlabel('GDP per Capita (inflation adjusted)', fontsize=12)
    plt.ylabel('Life Expectancy (years)', fontsize=12)
    
    # X ekseni logaritmik ölçeğe çevriliyor (Gelir verileri üstel dağılıma sahip olduğu için)
    plt.xscale('log')
    
    # Izgara ekle
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Renk çubuğu ekle
    cbar = plt.colorbar(scatter)
    cbar.set_label('Country Index', fontsize=10)
    
    # Belirli ülkeleri etiketle
    for i, country in enumerate(valid_countries):
        if country in ['United States', 'France', 'Japan', 'China', 'India', 'United Kingdom', 
                      'Germany', 'Turkey', 'Russia', 'Brazil']:
            plt.annotate(
                country,
                (valid_income[i], valid_life[i]),
                fontsize=8,
                xytext=(5, 5),
                textcoords='offset points'
            )
    
    # Grafiği ekrana göster
    plt.tight_layout()
    plt.show()
    
    # Bilgilendirici bir mesaj yazdır
    print("Note: The scatter plot shows the relationship between GDP per capita and life expectancy.")
    print("In general, countries with higher GDP per capita tend to have higher life expectancy,")
    print("suggesting a positive correlation between economic prosperity and health outcomes.")

# Ana fonksiyonu çalıştır
if __name__ == "__main__":
    main()
