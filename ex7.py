tongtien=int(input("ban da co bao nhieu tien ??? "))
songuoidonghop=0

while tongtien<100000 :
    dongop=int(input("moi bro quyen gop"))
    tongtien+=dongop
    if tongtien >100000:continue #dark dark
    songuoidonghop+=1
else:
    print("ban da co du tien moi` moi nguoi uong caphe quyen gop lam gi")
print("Da quen gop duoc {} tu {} nguoi " .format(tongtien,songuoidonghop))    