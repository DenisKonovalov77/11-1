import matplotlib.pyplot as plt
import pandas as pd
import requests

x = [-3, -2, -1, 0, 1, 2, 3]
y = [2, -2, 2, -2, 2, -2, 2]

plt.plot(x, y, marker='1')

plt.title('график функции')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)

plt.show()
print("\n код matplotlib закончен  \n")

Data = [7, 10, 17, 4, 13, 11, 9]
s = pd.Series(Data)
Index = ['а', 'б', 'в', 'г', 'д', 'е', 'ж']
si = pd.Series(Data, Index)
print(si)
print("\n код pandas закончен \n")

response = requests.get('https://api.github.com')
print(response.json())
print("\n код requests закончен \n")