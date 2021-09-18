import random
i=1
ds={}
while(i<=10):
    a=random.randint(1,100)
    ds.update({i:a})
    i=i+1
print(ds)