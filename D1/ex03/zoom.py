import numpy as np
import matplotlib.pyplot as plt
from load_image import ft_load

def main():
    """
    animal.jpeg görüntüsünü yükler, bilgilerini görüntüler ve yakınlaştırma yapar.
    """
    try:
        # Görüntüyü yükle
        image_array = ft_load("animal.jpeg")

        # Yükleme başarısız olduysa çık
        if image_array is None:
            return

        # Görüntünün bir bölgesini seç (zoom yapma)
        # Bu örnekte, görüntünün merkezinden 400x400 piksellik bir alan seçiyoruz
        height, width = image_array.shape[0], image_array.shape[1]

        # Merkezi bul
        center_y, center_x = height // 2, width // 2

        # 400x400 piksellik bir alan seç
        zoom_size = 200  # Merkezden her yöne 200 piksel (toplam 400x400)

        # Slice koordinatlarını hesapla
        y_start = max(0, center_y - zoom_size)
        y_end = min(height, center_y + zoom_size)
        x_start = max(0, center_x - zoom_size)
        x_end = min(width, center_x + zoom_size)

        # Görüntüyü dilimle
        zoomed_image = image_array[y_start:y_end, x_start:x_end]

        # Tek kanala indir (gri tonlama)
        if len(zoomed_image.shape) == 3 and zoomed_image.shape[2] == 3:
            # RGB görüntüyü gri tonlamaya çevir
            zoomed_image_gray = zoomed_image[:, :, 0:1]  # Sadece ilk kanalı al
            print(f"New shape after slicing: {zoomed_image_gray.shape}")
            print(zoomed_image_gray)
        else:
            print(f"New shape after slicing: {zoomed_image.shape}")
            print(zoomed_image)

        # Orijinal görüntüyü göster
        plt.figure(figsize=(12, 6))

        plt.subplot(1, 2, 1)
        plt.title("Orijinal Görüntü")
        plt.imshow(image_array)
        plt.colorbar()

        # Yakınlaştırılmış görüntüyü göster
        plt.subplot(1, 2, 2)
        plt.title("Yakınlaştırılmış Görüntü")

        if len(zoomed_image.shape) == 3 and zoomed_image.shape[2] == 3:
            plt.imshow(zoomed_image)
        elif len(zoomed_image.shape) == 3 and zoomed_image.shape[2] == 1:
            plt.imshow(zoomed_image_gray[:, :, 0], cmap='gray')
        else:
            plt.imshow(zoomed_image, cmap='gray')

        plt.colorbar()

        # Görüntüyü ekranda göster
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Programda bir hata oluştu: {e}")

if __name__ == "__main__":
    main()
