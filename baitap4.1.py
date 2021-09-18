i=1
dssv=[]
while  i<=5: 
 hoten =input("nhap ho ten: ")
 dssv.append(hoten)
 i=i+1
print(dssv)
vitri=int(input("nhap vi tri muon chinh sua"))
hoten=input("nhap ho ten moi")
dssv[vitri]=hoten
print(dssv)
print(dssv.sort())

