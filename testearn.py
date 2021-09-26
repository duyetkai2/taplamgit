str = str(input())
lst=[]
def chuoi(str):
    for i in str.split():
        if len(i)>3:
            lst.append(i)
chuoi(str)