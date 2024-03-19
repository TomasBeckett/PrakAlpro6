n = int(input("masukan bilangan n = "))

for i in range(n, 0, -1):
    faktorial = 1
    for j in range(i, 0, -1):
        faktorial *= j
    
    angka_menurun = ' '.join(str(k) for k in range(i, 0, -1))
    print(f"{faktorial} {angka_menurun}")







