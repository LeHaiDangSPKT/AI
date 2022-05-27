#%% 1. Cho numpy array có các phần tử: [-2 6 3 10 15 48], viết lệnh (không sử dụng vòng lặp) để lấy ra các bộ phần tử: [3 15], [6 10 48], [10 15 48], [48 15 10]. Gợi ý: slicing Python.
import numpy as np
arr = np.array([-2,6,3,10,15,48])
print(arr[2:5:2])
print(arr[1::2])
print(arr[3::])
print(arr[:-4:-1])
#%% 2. Tạo một 2D numpy array và thử dùng các hàm max(), max(0), max(1) để để thấy sự khác biệt. Cú pháp: ten_mang.max().
import numpy as np
arr = np.array([(4,5,6),(1,2,3)])
print(arr.max())
print(arr.max(0))
print(arr.max(1))
#%% 3. Giải phương trình
import math
def GiaiPT(arr):
    if (len(arr)==2):
        GiaiPTBac1(arr)
    else:
        GiaiPTBac2(arr)

def GiaiPTBac1(arr):
    if (arr[0] == 0):
        if (arr[1]==0):
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        print("Phương trình có nghiệm là: ", -arr[1]/arr[0])
def GiaiPTBac2(arr):
    if (arr[0] == 0):
        GiaiPTBac1(arr[1:])
    else:
        delta = arr[1]**2 - 4*arr[0]*arr[2]
        if (delta < 0):
            print("Phương trình vô nghiệm")
        elif (delta == 0):
            print("Phương trình có nghiệm kép, x = ", -arr[1]/(2*arr[0]))
        else:
            print("Nghiệm thứ nhất, x1 = ", (-arr[1] - math.sqrt(delta))/(2*arr[0]) )
            print("Nghiệm thứ hai, x2 = ", (-arr[1] + math.sqrt(delta))/(2*arr[0]) )

flag = True
while(flag):
    arr = list(map(float, input("Nhập các hệ số của phương trình: ").split()))
    if(len(arr)==2 or len(arr)==3):
        flag = False
    else:
        print("Thừa hoặc thiếu hệ số. Mời bạn nhập lại.")
GiaiPT(arr)
#%% 4. Sắp xếp (List)
def SapXep(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr)):
            if (arr[i] < arr[j]):
                arr[i], arr[j] = arr[j], arr[i]
    print(arr)

SapXep([7,8,9,6,2,1,5])
#%% 5. Sắp xếp (Numpy)
import numpy as np

def SapXep(arr, flag):
    if (flag):
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if (arr[i] < arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
    else:
        for i in range(0, len(arr)):
            for j in range(0, len(arr)):
                if (arr[i] > arr[j]):
                    arr[i], arr[j] = arr[j], arr[i]
    print(arr)
flag = input() == "" or input() == "SapXeptang"
arr = np.array([4,3,5,6])
SapXep(arr, flag)
# %%
