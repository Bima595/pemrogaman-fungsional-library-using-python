class Buku:
    def __init__(self, judul, status="tersedia"):
        self.title = judul
        self.status = status

    def __str__(self):
        return self.title


def tambah_buku(buku, daftar_buku):
    return daftar_buku + [buku]


def pinjam_buku(title, daftar_buku):
    def update_buku(buku):
        if buku.judul == title and buku.status == "tersedia":
            return Buku(buku.title, "dipinjam")
        return buku

    return list(map(update_buku, daftar_buku))


def kembalikan_buku(title, daftar_buku):
    def update_buku(buku):
        if buku.title == title and buku.status == "dipinjam":
            return Buku(buku.title, "tersedia")
        return buku

    return list(map(update_buku, daftar_buku))


def tampilkan_buku(daftar_buku):
    for buku in daftar_buku:
        print(f"{buku.title} ({buku.status})")


def main():
    daftar_buku = []

    while True:
        print("\nMenu:")
        print("1. Tambah Buku (Admin)")
        print("2. Pinjam Buku (User)")
        print("3. Kembalikan Buku (User)")
        print("4. Tampilkan Buku")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == "1":
            title = input("Masukkan judul buku: ")
            buku_baru = Buku(title)
            daftar_buku = tambah_buku(buku_baru, daftar_buku)

        elif pilihan == "2":
            title = input("Masukkan judul buku yang ingin dipinjam: ")
            daftar_buku = pinjam_buku(title, daftar_buku)

        elif pilihan == "3":
            title = input("Masukkan judul buku yang ingin dikembalikan: ")
            daftar_buku = kembalikan_buku(title, daftar_buku)

        elif pilihan == "4":
            tampilkan_buku(daftar_buku)

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
