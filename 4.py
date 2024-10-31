a = int(input("a :"))
b = int(input("b :"))
c = int(input("c :"))
if a > 0 and b > 0 and c > 0:
    if a**2 + b**2 == c**2:
        print("tam giac vuong")
    elif a == b != c:
        print("tam giac can")
    elif a == b == c:
        print("tam giac deu")
    elif a + b < c:
        print("khong la tam giac")
    elif a + b > c:
        print("tam giac thuong")
    else :
        print("idK")
