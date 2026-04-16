total = 0

while total < 800:
    tambah = int(input("Masukkan jumlah liter air: "))
    total += tambah

    if total == 800:
        print("Proses Selesai: Tangki Tepat Penuh")
    elif total > 800:
        print("Peringatan: Meluap! Air Berlebih", total - 800, "liter")
        break