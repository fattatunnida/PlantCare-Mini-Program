from datetime import datetime, timedelta

plants = []


def tambah_tanaman():
    print("\n=== TAMBAH TANAMAN ===")

    nama = input("Nama tanaman: ")
    jenis = input("Jenis tanaman: ")
    interval = int(input("Interval penyiraman (hari): "))
    tanggal = input("Terakhir disiram (YYYY-MM-DD): ")

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

    # FAULT 1
    # Langsung mengambil data pertama tanpa mengecek
    # apakah list masih kosong.
    plant = plants[0]

    print("Nama     :", plant["nama"])
    print("Jenis    :", plant["jenis"])
    print("Interval :", plant["interval"], "hari")


def cek_jadwal():
    print("\n=== JADWAL PENYIRAMAN ===")

    for plant in plants:
        last_watered = datetime.strptime(
            plant["terakhir_disiram"],
            "%Y-%m-%d"
        )

        # FAULT 2
        # Seharusnya + interval,
        # tetapi dibuat interval - 1.
        next_watered = last_watered + timedelta(
            days=plant["interval"] - 1
        )

        print(
            plant["nama"],
            "perlu disiram pada",
            next_watered.strftime("%Y-%m-%d")
        )


def cari_tanaman():
    print("\n=== CARI TANAMAN ===")

    search = input("Masukkan nama tanaman: ")

    for plant in plants:

        # FAULT 3
        # Perbandingan bersifat case-sensitive.
        if search == plant["nama"]:
            print("Tanaman ditemukan!")
            print("Nama :", plant["nama"])
            print("Jenis:", plant["jenis"])
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