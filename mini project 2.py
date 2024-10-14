from prettytable import PrettyTable

# Data admin dan anggota
user = {
    "admin": {"username": "rere", "password": "123"},
    "anggota": {"username": "lala", "password": "456"}
}

# Inisialisasi data calon ketua dan jumlah suara
Calon_ketua = [
    {"No Urut": "001", "Nama calon ketua": "Kim Dahyun", "Suara": 0},
    {"No Urut": "002", "Nama calon ketua": "Jeong Jaehyun", "Suara": 0},
    {"No Urut": "003", "Nama calon ketua": "Na Jaemin", "Suara": 0},
]

# Fungsi untuk menampilkan data calon ketua
def tampilkan_Calon_ketua():
    table = PrettyTable()
    table.field_names = ["No Urut", "Nama calon ketua", "Suara"]
    for item in Calon_ketua:
        table.add_row([item["No Urut"], item["Nama calon ketua"], item["Suara"]])
    print(table)

# Fungsi untuk menambahkan data calon ketua
def tambahkan_Calon_ketua():
    No_Urut = input("Masukkan No Urut: ")
    nama_calon_ketua = input("Masukkan Nama calon ketua: ")
    Calon_ketua.append({"No Urut": No_Urut, "Nama calon ketua": nama_calon_ketua, "Suara": 0})
    print("Calon berhasil ditambahkan!")

# Fungsi untuk mengupdate data calon ketua
def update_Calon_ketua():
    No_Urut = input("Masukkan No urut yang akan diupdate: ")
    for item in Calon_ketua:
        if item["No Urut"] == No_Urut:
            item["Nama calon ketua"] = input("Masukkan Nama calon ketua baru: ")
            print("Calon berhasil diupdate!")
            return
    print("Calon tidak ditemukan.")

# Fungsi untuk menghapus data calon ketua
def hapus_Calon_ketua():
    No_Urut = input("Masukkan No urut yang akan dihapus: ")
    for item in Calon_ketua:
        if item["No Urut"] == No_Urut:
            Calon_ketua.remove(item)
            print("Calon berhasil dihapus!")
            return
    print("Calon tidak ditemukan.")

# Fungsi untuk pemilihan calon ketua
def pemilihan_calon_ketua():
    tampilkan_Calon_ketua()
    pilihan = input("Masukkan No Urut calon yang dipilih: ")
    for item in Calon_ketua:
        if item["No Urut"] == pilihan:
            item["Suara"] += 1
            print(f"Anda telah memilih {item['Nama calon ketua']}.")
            return
    print("Pilihan tidak valid.")

# Fungsi untuk melihat hasil voting
def lihat_hasil_voting():
    print("\n==========| Hasil Voting |==========")
    tampilkan_Calon_ketua()

# Fungsi untuk login
def login(role):
    username = input("Masukkan username: ")
    password = input("Masukkan password: ")
    if username == user[role]["username"] and password == user[role]["password"]:
        print("Login berhasil!")
        return True
    else:
        print("Login gagal, periksa username dan password.")
        return False

# Fungsi utama program
def main():
    while True:
        print("\n==========| Calon pemilihan ketua |==========")
        print("1. Admin")
        print("2. Anggota")
        print("3. Keluar")
        pilihan = input("Pilih Role Anda (1/2/3): ")

        if pilihan == "1" and login("admin"):
            while True:
                print("\n==========| Menu Admin |==========")
                print("1. Tampilkan Data calon ketua")
                print("2. Tambahkan Data calon ketua")
                print("3. Update Data calon ketua")
                print("4. Hapus Data calon ketua")
                print("5. Lihat Hasil Voting")
                print("6. Kembali ke Menu Utama")
                admin_pilihan = input("Pilih Menu Admin (1/2/3/4/5/6): ")

                if admin_pilihan == "1":
                    tampilkan_Calon_ketua()
                elif admin_pilihan == "2":
                    tambahkan_Calon_ketua()
                elif admin_pilihan == "3":
                    update_Calon_ketua()
                elif admin_pilihan == "4":
                    hapus_Calon_ketua()
                elif admin_pilihan == "5":
                    lihat_hasil_voting()
                elif admin_pilihan == "6":
                    break
                else:
                    print("Pilihan tidak valid.")

        elif pilihan == "2" and login("anggota"):
            pemilihan_calon_ketua()
        elif pilihan == "3":
            print("Terima kasih telah memberikan suara.")
            break
        else:
            print("Pilihan tidak valid.")
main()


