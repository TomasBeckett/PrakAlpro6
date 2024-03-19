def prima(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def cari_prima(num):
    for i in range(num - 1, 1, -1):
        if prima(i):
            return i
    return None

n = int(input("Masukkan bilangan n: "))
prima_terdekat = cari_prima(n)

if prima_terdekat:
    print(f"Bilangan prima terdekat < {n} adalah {prima_terdekat}")
else:
    print(f"Tidak ditemukan bilangan prima terdekat < {n}")
