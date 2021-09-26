def luythua(n):
    x=lambda x:x**n
    return x
tinhmu=luythua(int(input("nhap so x")))
print(tinhmu(int(input("nhap mu n"))))

print("**********************************")
def hellos(dssv):
    for sv in dssv:
        print(f"Hello{sv}")
hellos(dssv="dark")
dssv=["asd","asdasdasd "]
hellos(dssv)




print("**********************************")
def thongtinsv(**sinhvien):
    if "hoten" in sinhvien.keys():
        print("Ho ten : {}".format(sinhvien["hoten"]))
    if "diachi" in sinhvien.keys():
        print("Dia chi : {}".format(sinhvien["diachi"]))
    if "tuoi" in sinhvien.keys():
        print("Tuoi : {}".format(sinhvien["tuoi"]))
    if "gioitinh" in sinhvien.keys():
        print("Gioi tinh : {}".format(sinhvien["gioitinh"]))
hoten2=str(input("nhap ho ten"))
diachi2=str(input("nhap dia chi"))
tuoi2=str(input("nhap tuoi"))
gioitinh2=str(input("nhap gioi tinh"))
thongtinsv(hoten=hoten2,diachi=diachi2,tuoi=tuoi2,gioitinh=gioitinh2)

print("**********************************")



def hello(*name):
    print('so lunog tham so {}'.format(len(name)))
    for x in name :
        print(f"xin chao{x}")
hello("hoa")
hello("hoa","hue","hong")
print("**********************************")




def sumf(a,b):
    print("tong cua {} va {} la".format(a,b),a+b)
a=int(input("nhap a"))
b=int(input("nhap b"))
sumf(a,b)
print("**********************************")
       
        