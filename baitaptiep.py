from typing import Match


import math
a =int(input("nhap a"))
b=int(input("nhap b"))
c =int(input("nhap c"))
delta=b*b-4*a*c
if a!=0:
        if delta >0:
            print("pt co 2 nghiem phan biet",(-b-math.sqrt(delta))/2*a,(-b+math.sqrt(delta))/2*a)
        if delta ==0:
            print("pt co 2 2 nghiem kep",-b/(2*a))
        else :
            print("pt vo nghiem")
else :
    print("pt co nghiem la "+str(-b/(2*a)))
