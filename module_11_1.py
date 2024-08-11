import requests
from pprint import pprint
import matplotlib.pyplot as plt
import pandas as pd

# библиотека requests позволяет быстро и просто формировать HTTP запросы,
# предоставлять ответ от сервера в удобном формате

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
url = 'https://github.com/timeline.json'

response = requests.get(url, headers=headers)
pprint(response.headers)
pprint(response.json())

# matplotlib - это пакет для визуализации данных в виде графиков, диаграмм и т.д.
x = [1, 2, 3, 4, 5, 6, 7]
y = [1, 4, 2, 3, 3, 2, 6]

plt.plot(x, y, color='red', marker='o', markersize=6)
plt.xlabel('ось Х')
plt.ylabel('ось У')
plt.title('просто график')
plt.bar(x, y)
plt.show()

# pandas - модуль для работы с таблицами (дата фреймами). Позволяет редактировать таблицы,
# извлекать данные из файлов CSV, excel, txt, json, а так же записывать данные в файлы этих форматов
data_1 = {'name': ['first', 'second', 'third', 'fourth'], 'old_price': [200, 412, 523, 111],
        'new_price': [323, 550, 1200, 540]}
df_1 = pd.DataFrame(data_1)
df_1.index = ['prod_1', 'prod_2', 'prod_3', 'prod_4']

print(df_1)
mean = df_1['old_price'].mean()
print(f'среднее значение столбца old_price: {mean}')
print()

data_2 = pd.read_csv('sample_1.csv')
df_2 = pd.DataFrame(data_2)

print(df_2)
max_new_price = df_2['new_price'].max()
print(f'Максиамльное значение в столбце new_price: {max_new_price}')
stat = df_1.describe()
print(stat)
df_1.to_csv('sample_2.txt')  # запись дата фрейма в txt файл
