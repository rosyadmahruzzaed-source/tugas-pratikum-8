class Mahasiswa:
    def __init__(self):
        self.data = []

    # METHOD TAMBAH
    def tambah(self, nama, nim, umur, alamat, nilai):
        self.data.append({
            "nama": nama,
            "nim": nim,
            "umur": umur,
            "alamat": alamat,
            "nilai": nilai
        })
        print(f"Data {nama} berhasil ditambahkan.\n")

    # METHOD TAMPILKAN
    def tampilkan(self):
        if not self.data:
            print("Tidak ada data mahasiswa.\n")
            return

        print("=== Daftar Nilai Mahasiswa ===")
        for i, mhs in enumerate(self.data, start=1):
            print(
                f"{i}. Nama: {mhs['nama']}, "
                f"NIM: {mhs['nim']}, "
                f"Umur: {mhs['umur']}, "
                f"Alamat: {mhs['alamat']}, "
                f"Nilai: {mhs['nilai']}"
            )
        print()

    # METHOD HAPUS
    def hapus(self, nama):
        for mhs in self.data:
            if mhs["nama"].lower() == nama.lower():
                self.data.remove(mhs)
                print(f"Data {nama} berhasil dihapus.\n")
                return
        print(f"Data dengan nama {nama} tidak ditemukan.\n")

    # METHOD UBAH
    def ubah(self, nama, nim_baru=None, umur_baru=None, alamat_baru=None, nilai_baru=None):
        for mhs in self.data:
            if mhs["nama"].lower() == nama.lower():
                if nim_baru:
                    mhs["nim"] = nim_baru
                if umur_baru:
                    mhs["umur"] = umur_baru
                if alamat_baru:
                    mhs["alamat"] = alamat_baru
                if nilai_baru is not None:
                    mhs["nilai"] = nilai_baru

                print(f"Data {nama} berhasil diubah.\n")
                return

        print(f"Data dengan nama {nama} tidak ditemukan.\n")


# ---------------------------
# PROGRAM UTAMA
# ---------------------------

m = Mahasiswa()

while True:
    print("=== MENU ===")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        umur = int(input("Masukkan umur: "))
        alamat = input("Masukkan alamat: ")
        nilai = float(input("Masukkan nilai: "))
        m.tambah(nama, nim, umur, alamat, nilai) 

    elif pilihan == "2":
        m.tampilkan()
  
    elif pilihan == "3":
        nama = input("Masukkan nama yang ingin dihapus: ")
        m.hapus(nama)

    elif pilihan == "4":
        nama = input("Masukkan nama yang ingin diubah: ")

        nim_baru = input("Masukkan NIM baru (kosongkan jika tidak diubah): ")
        umur_baru = input("Masukkan umur baru (kosongkan jika tidak diubah): ")
        alamat_baru = input("Masukkan alamat baru (kosongkan jika tidak diubah): ")
        nilai_input = input("Masukkan nilai baru (kosongkan jika tidak diubah): ")

        nim_baru = nim_baru if nim_baru else None
        umur_baru = int(umur_baru) if umur_baru else None
        alamat_baru = alamat_baru if alamat_baru else None
        nilai_baru = float(nilai_input) if nilai_input else None

        m.ubah(nama, nim_baru, umur_baru, alamat_baru, nilai_baru)

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.\n")
