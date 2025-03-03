import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

def ft_load(path: str) -> np.ndarray:
    """
    Verilen yoldan bir görüntüyü yükler ve NumPy dizisi olarak döndürür.

    Parametreler:
        path (str): Yüklenecek görüntünün dosya yolu

    Dönüş:
        np.ndarray: Yüklenen görüntüye karşılık gelen NumPy dizisi

    Hatalar:
        - Dosya bulunamazsa bilgilendirici bir hata mesajı verir
        - Görüntü yüklenemezse bilgilendirici bir hata mesajı verir
    """
    try:
        # Dosyanın var olduğunu kontrol et
        if not os.path.exists(path):
            print(f"Hata: '{path}' dosyası bulunamadı.")
            return None

        # Görüntüyü yükle
        image = Image.open(path)

        # NumPy dizisine dönüştür
        array = np.array(image)

        # Görüntü boyutunu yazdır
        print(f"The shape of image is: {array.shape}")

        # Piksel içeriğini yazdır
        print(array)

        return array

    except Exception as e:
        print(f"Görüntü yüklenirken bir hata oluştu: {e}")
        return None
