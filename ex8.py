for x in range(5):
    print(x)
    if x==2:break
else:
    print("vong lap ket thuc tai x = {}".format(x))

dssinhvien =["An","Khanh","Minh","Linh","Ty"]
for sinhvien in dssinhvien :
    print(sinhvien)

for char in dssinhvien[1]:
    print(char)
tong =0
for i in range(11) :
    tong=tong+i
print(f"tong tu 0-10 la : {tong}")