import pandas as pd
import numpy as np
import tkinter as tk
from tkinter import ttk

# Excel dosyasını oku
file_path = 'C:\\Users\\Meltem\\Desktop\\soru1_2_data.xlsx'
data = pd.read_excel(file_path, header=None)

# Veri çerçevesini numpy array'e çevir
image = data.to_numpy()

# Piksel değerlerinin histogramını hesapla
hist, bin_edges = np.histogram(image, bins=np.arange(257))

# Kümülatif Dağılım Fonksiyonunu (CDF) hesapla
cdf = hist.cumsum()

# CDF'yi normalize et
cdf_normalized = cdf * (255 / cdf[-1])

# Yeni piksel değerlerini hesapla
equalized_image = np.interp(image.flatten(), bin_edges[:-1], cdf_normalized)

# Yeni piksel değerlerini 32x32 matrisine geri döndür
equalized_image = equalized_image.reshape(image.shape)

# Tkinter GUI ile tablo gösterme
def show_table(data, title):
    root = tk.Tk()
    root.title(title)

    frame = ttk.Frame(root, padding=10)
    frame.grid(row=0, column=0)

    tree = ttk.Treeview(frame, columns=[f'Col {i+1}' for i in range(data.shape[1])], show='headings')

    for i in range(data.shape[1]):
        tree.heading(f'Col {i+1}', text=f'Col {i+1}')
        tree.column(f'Col {i+1}', width=50)

    for row in data:
        tree.insert('', tk.END, values=row)

    tree.grid(row=0, column=0)

    scrollbar = ttk.Scrollbar(frame, orient=tk.VERTICAL, command=tree.yview)
    tree.configure(yscroll=scrollbar.set)
    scrollbar.grid(row=0, column=1, sticky='ns')

    root.mainloop()

# Orijinal Görüntü
print("Orijinal Görüntü:")
print(image)
show_table(image, "Orijinal Görüntü")

# Piksel Değerleri ve Frekans
hist_data = np.column_stack((bin_edges[:-1], hist))
print("\nPiksel Değerleri ve Frekans:")
print(hist_data)
show_table(hist_data, "Piksel Değerleri ve Frekans")

# Kümülatif Dağılım Fonksiyonu (CDF)
cdf_data = np.column_stack((bin_edges[:-1], cdf))
print("\nKümülatif Dağılım Fonksiyonu (CDF):")
print(cdf_data)
show_table(cdf_data, "Kümülatif Dağılım Fonksiyonu (CDF)")

# Eşitlenmiş Piksel Değerleri (CDF Normalized)
cdf_normalized_data = np.column_stack((bin_edges[:-1], cdf_normalized))
print("\nEşitlenmiş Piksel Değerleri (CDF Normalized):")
print(cdf_normalized_data)
show_table(cdf_normalized_data, "Eşitlenmiş Piksel Değerleri (CDF Normalized)")

# Yeni Piksel Değerleri ve Frekans (Equalized Image)
equalized_data = np.column_stack(np.unique(equalized_image, return_counts=True))
print("\nYeni Piksel Değerleri ve Frekans (Equalized Image):")
print(equalized_data)
show_table(equalized_data, "Yeni Piksel Değerleri ve Frekans (Equalized Image)")

# Eşitlenmiş Görüntü
print("\nEşitlenmiş Görüntü:")
print(equalized_image.astype(np.uint8))
show_table(equalized_image.astype(np.uint8), "Eşitlenmiş Görüntü")
