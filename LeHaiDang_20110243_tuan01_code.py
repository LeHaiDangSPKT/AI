
#%% 4. a) Viết chương trình tìm max trong 4 số được nhập bởi người dùng.  
def timMax(a,b,c,d):
    max = a
    if (b > max):
        max = b
    if (c > max):
        max = c
    if (d > max):
        max = d
    return max

print("Nhập số thứ nhất: ")
a = (float)(input())
print("Nhập số thứ hai: ")
b = (float)(input())
print("Nhập số thứ ba: ")
c = (float)(input())
print("Nhập số thứ tư: ")
d = (float)(input())

print("Số lớn nhất trong bốn số là: ", timMax(a,b,c,d))
#%% 4. b) Viết chương trình giải phương trình bậc 1.
print("GIẢI PHƯƠNG TRÌNH BẬC NHẤT: a.x + b = 0")
print("Nhập a: ")
a = (float)(input())
print("Nhập b: ")
b = (float)(input())

if (a == 0):
    if (b == 0):
        print("Phương trình vô số nghiệm !")
    else:
        print("Phương trình vô nghiệm !")
else:
    print("Phương trình có nghiệm: ", -b/a)
# %% 4. c) Viết chương trình giải phương trình bậc 2.
import math
print("GIẢI PHƯƠNG TRÌNH BẬC HAI: a.x^2 + b.x + c = 0")
print("Nhập a: ")
a = (float)(input())
print("Nhập b: ")
b = (float)(input())
print("Nhập c: ")
c = (float)(input())

if (a == 0):
    if (b == 0):
        if (c == 0):
            print("Phương trình vô số nghiệm !")
        else:
            print("Phương trình vô nghiệm !")
    else:
        print("Phương trình có một nghiệm đơn: " -c/b)
else:
    delta = b*b - 4*a*c
    if (delta < 0):
        print("Phương trình vô nghiệm !")
    elif (delta == 0):
        print("Phương trình có nghiệm kép: ", -b/(2*a))
    else:
        print("Nghiệm thứ nhất: ", (float)((-b - math.sqrt(delta))/(2*a)))
        print("Nghiệm thứ hai: ", (float)((-b + math.sqrt(delta))/(2*a)))

# %% 4. d) Viết chương trình in ra học lực theo điểm số được nhập bởi người dùng.
flag = True
while(flag):
    print("Nhập điểm trung bình của bạn: ")
    dtb = (float)(input())
    if (dtb >= 0 and dtb <= 10):
        flag = False
    else:
        print("Điểm không hợp lệ, mời bạn nhập lại !")

if (dtb < 4):
    print("Học lực kém.")
elif (dtb < 5):
    print("Học lực yếu.")
elif (dtb < 6):
    print("Học lực trung bình.")
elif (dtb < 7):
    print("Học lực trung bình khá.")
elif (dtb < 8):
    print("Học lực khá.")
elif (dtb < 9):
    print("Học lực giỏi.")
else:
    print("Học lực xuất sắc.")


# %%
