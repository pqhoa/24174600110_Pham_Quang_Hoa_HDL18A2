print("Nhap toa do I:")
x = input("x = ")
y = input("y = ")
print("Nhap toa do M:")
a = input("a = ")
b = input("b = ")
print("gia tri r:")
r = input("r = ")

x = float(x)
y = float(y)
a = float(a)
b = float(b)
r = float(r)

#xét kc từ r đến đường tròn
IM = ((x - a)**2 + (y - b)**2)**(1/2)

if IM > r:
   print("M_k_thuoc_dg_tron")
elif IM < r:
   print("M nam trong duong tron")
else:
    print("M thuoc dg tron")



