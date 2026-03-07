from datetime import datetime
GAJI_POKOK = {
    "A": 2_500_000,
    "B": 2_000_000,
    "C": 1_500_000
}

LEMBUR_PER_JAM = {
    "A": 30_000,
    "B": 20_000,
    "C": 15_000
}


def input_golongan():
    while True:
        g = input("Golongan (A/B/C): ").strip().upper()
        if g in GAJI_POKOK:
            return g
        print("Golongan tidak valid. Masukkan A, B, atau C.")


def input_jam_kerja():
    while True:
        try:
            jam = float(input("Jam kerja (>=0): "))
            if jam >= 0:
                return jam
            print("Jam kerja harus >= 0.")
        except ValueError:
            print("Input jam kerja harus angka.")


def hitung_gaji(golongan, jam_kerja):
    gaji_pokok = GAJI_POKOK[golongan]
    jam_lembur = max(0, jam_kerja - 40)
    uang_lembur = jam_lembur * LEMBUR_PER_JAM[golongan]
    total_gaji = gaji_pokok + uang_lembur
    return gaji_pokok, jam_lembur, uang_lembur, total_gaji


def input_tanggal_gajian():
    today = datetime.now()
    tanggal_gajian = datetime(today.year, today.month, 30)
    return tanggal_gajian.strftime("%d-%m-%Y")


def main():
    print("=== PENGHITUNG GAJI KARYAWAN ===")

    tanggal_gajian = input_tanggal_gajian()
    print(f"Tanggal Gajian : {tanggal_gajian}\n")

    while True:
        try:
            n = int(input("Jumlah karyawan: "))
            if n > 0:
                break
            print("Jumlah karyawan harus > 0.")
        except ValueError:
            print("masukan hanya bisa angka")

    data = []

    for i in range(1, n + 1):
        print(f"\n-- Data karyawan ke-{i} --")
        nama = input("Nama: ").strip()
        gol = input_golongan()
        jam = input_jam_kerja()

        gaji_pokok, jam_lembur, uang_lembur, total = hitung_gaji(gol, jam)
        data.append({
            "nama": nama,
            "gol": gol,
            "jam": jam,
            "gaji_pokok": gaji_pokok,
            "jam_lembur": jam_lembur,
            "uang_lembur": uang_lembur,
            "total": total,
            "tanggal_gajian": tanggal_gajian
        })

        print("\n===== RINCIAN GAJI =====")
    for d in data:
        print(
            f"{'Nama':15}: {d['nama']}\n"
            f"{'Golongan':15}: {d['gol']}\n"
            f"{'Jam kerja':15}: {d['jam']}\n"
            f"{'Gaji pokok':15}: Rp {d['gaji_pokok']:,}\n"
            f"{'Lembur':15}: {d['jam_lembur']} jam x Rp {LEMBUR_PER_JAM[d['gol']]:,} = Rp {d['uang_lembur']:,}\n"
            f"{'Total gaji':15}: Rp {d['total']:,}\n"
            f"{'Tanggal gajian':15}: {d['tanggal_gajian']}\n"
            + "-" * 40
        )

    total_penggajian = sum(d["total"] for d in data)
    print(f"\nTOTAL PENGGAJIAN (semua karyawan): {total_penggajian}")

if __name__ == "__main__":
    main()