#%% Bài 1
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import axes3d
from matplotlib import cm, projections
from math import e

x = np.linspace(-2, 2, 50)
y = np.linspace(-2, 2, 50)
x, y = np.meshgrid(x, y)

z = x*e**(-x**2 - y**2)

%matplotlib qt
fig = plt.figure()
ax = fig.gca(projection='3d')
surf = ax.plot_surface(x,y,z, cmap = cm.jet)

fig.colorbar(surf)

ax.set_xlabel('Ox')
ax.set_ylabel('Oy')
ax.set_zlabel('Oz')
ax.set_title('Hàm x.e^(-x^2 - y^2)')

plt.show()
# %% Bài 2 a+b
import pandas as pd

people = pd.read_csv('../data.csv', encoding='utf-8', sep=',')

# people.head(2)
# people.describe()
# people.info()
# people.iloc[[0]]       #Hàng
# people.iloc[:, [0]]    #Cột
people.iloc[[1], [0]]    #Phần tử
# %% Bài 2 c
people = pd.read_csv('../Data_DanSo.csv', encoding='utf-8', sep=',')

y = []
x = np.arange(2016, 2019, 1)
arr = people.iloc[[2]]
for i, row in arr.iterrows():
    for j, column in row.iteritems():
        y.append(column)

plt.title('Đồ thị dân số của ' + y.pop(0) + ' từ năm 2016 đến 2018')
plt.plot(x,y, 'go-', label='Dân số trung bình')
plt.xlabel('Năm')
plt.ylabel('Nghìn người')

plt.show()

# %% Bài 3
import my_package as mp
x = 2
y = 0

a = mp.Cong2So(x,y)
b = mp.Tru2So(x,y)
c = mp.Nhan2So(x,y)
d = mp.Chia2So(x,y)

# %% Bài 4
import sympy as sp

y = '5*x**2 +6*x - 37'
print(sp.solve(y, 'x'))

y = '2*x**3 - x'
print(sp.solve(y, 'x'))

y = 'u*x**2 + v*x'
print(sp.solve(y, 'x'))
print(sp.solve(y, 'u'))
print(sp.solve(y, 'v'))

# %% Bài 6
from sympy import sin, cos
from sympy.abc import x,y,u,v

y = sin(u*x)*cos(v*x)

answer_1 = sp.diff(y, x)
answer_2 = sp.diff(y, x, 2)
answer_3 = sp.diff(y, u)

print(answer_1)
print(answer_2)
print(answer_3)



# %%
