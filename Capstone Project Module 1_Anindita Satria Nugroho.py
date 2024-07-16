from tabulate import tabulate

# Data pasien disimpan dalam list
data_pasien = []

# Fungsi CREATE untuk menambahkan pasien
def tambah_pasien():
    nama = input("Masukkan nama pasien: ")
    umur = input("Masukkan umur pasien: ")
    keluhan = input("Masukkan keluhan pasien: ")
    no_hp = input("Masukkan nomor HP pasien: ")

    if not nama or not umur.isdigit() or not keluhan or not no_hp.isdigit():
        print("\nInput tidak valid. Pastikan semua informasi diisi dengan benar (khusus untuk Umur dan No. HP wajib diisi menggunakan angka).")
        return
    
    pasien_baru = {
        'ID': len(data_pasien) + 1,
        'Nama': nama,
        'Umur': int(umur),
        'Keluhan': keluhan,
        'No. HP': no_hp
    }
    data_pasien.append(pasien_baru)
    print("Pasien berhasil ditambahkan.")

# Fungsi READ untuk menampilkan semua pasien
def tampilkan_pasien():
    if data_pasien:
        print(tabulate(data_pasien, headers="keys", tablefmt="grid"))
    else:
        print("\nBelum ada data pasien. Silahkan masukan data pasien terlebih dahulu.")

# Fungsi UPDATE untuk memperbarui data pasien
def perbarui_pasien():
    try:
        id_pasien = int(input("Masukkan ID pasien yang akan diperbarui: "))
        nama = input("Masukkan nama baru (biarkan kosong jika tidak diubah): ")
        umur = input("Masukkan umur baru (biarkan kosong jika tidak diubah): ")
        keluhan = input("Masukkan keluhan baru (biarkan kosong jika tidak diubah): ")
        no_hp = input("Masukkan nomor HP baru (biarkan kosong jika tidak diubah): ")

        for pasien in data_pasien:
            if pasien['ID'] == id_pasien:
                if nama:
                    pasien['Nama'] = nama
                if umur and umur.isdigit():
                    pasien['Umur'] = int(umur)
                if keluhan:
                    pasien['Keluhan'] = keluhan
                if no_hp:
                    pasien['No. HP'] = no_hp
                print("Data pasien berhasil diperbarui.")
                return
        print("Pasien dengan ID tersebut tidak ditemukan.")
    except ValueError:
        print("ID pasien harus berupa angka.")

# Fungsi DELETE untuk menghapus pasien
def hapus_pasien():
    try:
        id_pasien = int(input("Masukkan ID pasien yang akan dihapus: "))
        global data_pasien
        data_pasien = [pasien for pasien in data_pasien if pasien['ID'] != id_pasien]
        print("Pasien berhasil dihapus.")
    except ValueError:
        print("ID pasien harus berupa angka.")

# Fungsi FILTER untuk menampilkan pasien berdasarkan kriteria
def filter_pasien():
    kriteria = input("Masukkan kriteria filter (Nama/Umur/Keluhan/No. HP): ").capitalize()
    nilai = input("Masukkan nilai filter: ").lower()
    
    hasil_filter = [pasien for pasien in data_pasien if nilai in str(pasien.get(kriteria, '')).lower()]
    
    if hasil_filter:
        print(tabulate(hasil_filter, headers="keys", tablefmt="grid"))
    else:
        print("Tidak ada pasien yang sesuai dengan kriteria filter.")


# Fungsi utama untuk menampilkan menu dan menangani input pengguna
def main():
    while True:
        print("\nMenu:")
        print("1. Tambah Pasien")
        print("2. Tampilkan Pasien")
        print("3. Filter Pasien")
        print("4. Perbarui Pasien")
        print("5. Hapus Pasien")
        print("6. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4/5/6): ")
        
        if pilihan == '1':
            tambah_pasien()
        elif pilihan == '2':
            tampilkan_pasien()
        elif pilihan == '3':
            filter_pasien()
        elif pilihan == '4':
            perbarui_pasien()
        elif pilihan == '5':
            hapus_pasien()
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid, silakan coba lagi.")
            
main()
