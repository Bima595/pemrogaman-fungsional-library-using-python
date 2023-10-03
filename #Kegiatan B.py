# Kegiatan B
class Buku:
    def __init__(self, judul, status="tersedia"):
        self.judul = judul
        self.status = status

    def __str__(self):
        return self.judul


def tambah_buku(buku, daftar_buku):
    return daftar_buku + [buku]


def pinjam_buku(judul, daftar_buku):
    def update_buku(buku):
        if buku.judul == judul and buku.status == "tersedia":
            return Buku(buku.judul, "dipinjam")
        return buku

    return list(map(update_buku, daftar_buku))


def kembalikan_buku(judul, daftar_buku):
    def update_buku(buku):
        if buku.judul == judul and buku.status == "dipinjam":
            return Buku(buku.judul, "tersedia")
        return buku

    return list(map(update_buku, daftar_buku))


def tampilkan_buku(daftar_buku):
    for buku in daftar_buku:
        print(f"{buku.judul} ({buku.status})")


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
            judul = input("Masukkan judul buku: ")
            buku_baru = Buku(judul)
            daftar_buku = tambah_buku(buku_baru, daftar_buku)

        elif pilihan == "2":
            judul = input("Masukkan judul buku yang ingin dipinjam: ")
            daftar_buku = pinjam_buku(judul, daftar_buku)

        elif pilihan == "3":
            judul = input("Masukkan judul buku yang ingin dikembalikan: ")
            daftar_buku = kembalikan_buku(judul, daftar_buku)

        elif pilihan == "4":
            tampilkan_buku(daftar_buku)

        elif pilihan == "5":
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()
