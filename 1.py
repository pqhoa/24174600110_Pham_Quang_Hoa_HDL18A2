# bài toán năm nhuan
print("nam:")
nam_nhuan = float(input("nhap vao nam nhuan: "))
if nam_nhuan / 4 == 0 and nam_nhuan % 100 != 0:
   print("nam_nhuan_roi")
elif nam_nhuan / 400 == 0:
    print("nam_nhuan")
else:
   print("nam_khong_nhuan")


