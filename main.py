import pandas as pd

# CSV faylini yuklash
df = pd.read_csv('ma'lumotlar.csv')

# CSV faylini ko'rish
print(df.head())

# Statistika chiqarish
print("Statistika:")
print(df.describe())

# Ma'lumotlar statistikasini chiqarish
print("Ma'lumotlar statistikasi:")
print(df.info())

# Ma'lumotlar statistikasini chiqarish
print("Ma'lumotlar statistikasi:")
print(df.describe(include='all'))

# Grafik chiqarish
import matplotlib.pyplot as plt

# Grafik chiqarish
df['sarlavha'].value_counts().plot(kind='bar')
plt.title('Sarlavha statistikasi')
plt.xlabel('Sarlavha')
plt.ylabel('Ko\'rinish')
plt.show()

# Grafik chiqarish
df['sarlavha'].value_counts().plot(kind='pie')
plt.title('Sarlavha statistikasi')
plt.show()
```

Kodni yozishda quyidagi qoidalar qo'llanganman:

1. Pandas kutubxonasini import qilganman.
2. CSV faylini yuklaganman.
3. CSV faylini ko'rganman.
4. Statistika chiqarilganman.
5. Ma'lumotlar statistikasini chiqarilganman.
6. Grafik chiqarilganman.
