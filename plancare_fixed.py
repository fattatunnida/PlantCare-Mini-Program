from datetime import datetime, timedelta

plants = []


def tambah_tanaman():
    print("\n=== TAMBAH TANAMAN ===")

    nama = input("Nama tanaman: ")
    jenis = input("Jenis tanaman: ")

    try:
        interval = int(input("Interval penyiraman (hari): "))
    except ValueError:
        print("Interval harus berupa angka.")
        return

    tanggal = input("Terakhir disiram (YYYY-MM-DD): ")

    try:
        datetime.strptime(tanggal, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal salah.")
        return

    plant = {
        "nama": nama,
        "jenis": jenis,
        "interval": interval,
        "terakhir_disiram": tanggal
    }

    plants.append(plant)

    print("Tanaman berhasil ditambahkan!")


def lihat_tanaman():
    print("\n=== DAFTAR TANAMAN ===")

    # PERBAIKAN FAULT 1
    # Mengecek apakah data masih kosong.
    if not plants:
        print("Belum ada data tanaman.")
        return

    for i, plant in enumerate(plants, start=1):
        print(f"\nTanaman {i}")
        print("Nama     :", plant["nama"])
        print("Jenis    :", plant["jenis"])
        print("Interval :", plant["interval"], "hari")
        print("Terakhir :", plant["terakhir_disiram"])


def cek_jadwal():
    print("\n=== JADWAL PENYIRAMAN ===")

    if not plants:
        print("Belum ada data tanaman.")
        return

    for plant in plants:
        last_watered = datetime.strptime(
            plant["terakhir_disiram"],
            "%Y-%m-%d"
        )

        # PERBAIKAN FAULT 2
        # Menggunakan interval sebenarnya.
        next_watered = last_watered + timedelta(
            days=plant["interval"]
        )

        print(
            plant["nama"],
            "perlu disiram pada",
            next_watered.strftime("%Y-%m-%d")
        )


def cari_tanaman():
    print("\n=== CARI TANAMAN ===")

    if not plants:
        print("Belum ada data tanaman.")
        return

    search = input("Masukkan nama tanaman: ")

    for plant in plants:

        # PERBAIKAN FAULT 3
        # Membuat pencarian tidak sensitif
        # terhadap huruf besar/kecil.
        if search.lower() == plant["nama"].lower():
            print("\nTanaman ditemukan!")
            print("Nama :", plant["nama"])
            print("Jenis:", plant["jenis"])
            print("Interval:", plant["interval"], "hari")
            return

    print("Tanaman tidak ditemukan.")


def main():
    while True:
        print("\n===== PLANTCARE =====")
        print("1. Tambah tanaman")
        print("2. Lihat daftar tanaman")
        print("3. Cek jadwal penyiraman")
        print("4. Cari tanaman")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tambah_tanaman()

        elif pilihan == "2":
            lihat_tanaman()

        elif pilihan == "3":
            cek_jadwal()

        elif pilihan == "4":
            cari_tanaman()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")


main()