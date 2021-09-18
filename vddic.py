sanpham={
    "thuonghieu":"apple",
     "sacnhanhh":True,
      "namsx":2021,
        "mausac":["do","vang","den"]
}
print(sanpham)

print(sanpham["thuonghieu"])
print(sanpham.keys())
print(sanpham.values())
sanpham.update({"thuonghieu":"android"})
sanpham.update({"cannang":"1.2Kg"})
print(sanpham)