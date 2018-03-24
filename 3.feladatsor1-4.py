def feladat_1(n):
    lst = []
    plst = []
    n = int(input("Mennyi?"))
    for i in range(n):
        y = int(input("Következő szám?"))
        lst.append(y)
    for i in range(1, n):
        if lst[i] == lst[i - 1]:
            plst.append((i, i - 1))

    print(plst)
def feladat_2():
    paros = 0
    paratlan = 0
    c = int(input("mennyi?"))
    for i in range(c):
        d = int(input("Kerem a szamot"))
        if d % 2 == 0:
            paros = paros + 1
        else:
            paratlan = paratlan + 1
    print("A páros:páratlan arány ", end="")
    print(paros, end="")
    print(":", end="")
    print(paratlan, end="")
    print(".", end="")
def feladat_3():
    lst=[]
    n=int(input("Hany?"))
    for i in range(n):
        x=int(input("Szam"))
        lst.append(abs(x))
    s=sum(lst)
    print(a/n)
def feladat_4():
    a = 1
    b = 0
    g = 0
    voltneg = False
    n = int(input("Hány?"))
    for i in range(n):
        x = int(input("Szám"))
        if x > 0:
            a = a * x
        elif x < 0:
            voltneg = True
            g = g + 1
            b = b + x
    if voltneg == False:
        print(a)
    else:
        print(a, b / g)






