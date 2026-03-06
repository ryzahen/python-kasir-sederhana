data_barang = {
1: ("Baju",10000),
2: ("Celana",30000),
3: ("Sepatu",25000),
4: ("Sandal",15000),
5: ("Topi",20000)
}

belanja = []

def tampil():
    print("---- PROGRAM KASIR TOKO ----")
    print("Kode | Barang | Harga")
    print("----")
    for k in data_barang:
        print(k,"|",data_barang[k][0],"|",data_barang[k][1])
    print("----")

def beli():
    while True:
        tampil()

        while True:
            try:
                pilih = int(input("Pilih kode barang : "))
                break
            except:
                print("Input harus angka")

        if pilih in data_barang:
            while True:
                try:
                    jumlah = int(input("Jumlah beli : "))
                    break
                except:
                    print("Input harus angka")

            harga = data_barang[pilih][1]
            total = harga * jumlah
            belanja.append(total)
        else:
            print("Kode tidak ada")

        lagi = input("Tambah barang? y/t : ")
        if lagi == "t":
            break

def diskon(total):
    if total > 200000:
        return total * 0.08
    elif total > 150000:
        return total * 0.05
    elif total > 100000:
        return total * 0.03
    elif total > 50000:
        return total * 0.01
    else:
        return 0

def bayar():
    print("---- RINCIAN ----")
    total = sum(belanja)
    print("Total belanja :", total)

    potongan = diskon(total)
    print("Diskon :", potongan)

    harus_bayar = total - potongan
    print("Total bayar :", harus_bayar)

    print("----")

    while True:
        try:
            uang = int(input("Uang bayar : "))
        except:
            print("Input harus angka")
            continue

        if uang < harus_bayar:
            print("Uang kurang, silakan masukkan lagi")
        else:
            break

    kembali = uang - harus_bayar
    print("Kembalian :", kembali)
    print("----")
    print("Terima kasih")

beli()
bayar()