## Tujuan Program

Program ini bertujuan untuk membantu admin Rumah Sakit mengelola data pasien dengan menyediakan fungsi untuk menambah, menampilkan, memperbarui, menghapus, dan memfilter data pasien. 
Program ini memudahkan pengguna untuk mengelola informasi pasien secara terstruktur dan efisien.

## Alur Program

1. **Memulai Program**
   - Program dimulai dengan menjalankan fungsi `main()`.
   - Menampilkan menu utama dengan pilihan untuk menambah, menampilkan, memfilter, memperbarui, menghapus pasien, atau keluar dari program.

2. **Tambah Pasien (CREATE)**
   - Pengguna memilih opsi "1" dari menu utama.
   - Fungsi `tambah_pasien()` meminta input nama, umur, keluhan, dan nomor HP pasien.
   - Memvalidasi input (umur dan nomor HP harus berupa angka).
   - Jika valid, data pasien baru ditambahkan ke dalam `data_pasien` dan pesan konfirmasi ditampilkan.

3. **Tampilkan Pasien (READ)**
   - Pengguna memilih opsi "2" dari menu utama.
   - Fungsi `tampilkan_pasien()` menampilkan semua data pasien yang tersimpan dalam `data_pasien` menggunakan tabel yang diformat oleh `tabulate`.
   - Jika tidak ada data pasien, menampilkan pesan bahwa belum ada data pasien yang tersimpan.

4. **Filter Pasien (FILTER)**
   - Pengguna memilih opsi "3" dari menu utama.
   - Fungsi `filter_pasien()` meminta input kriteria filter (Nama, Umur, Keluhan, No. HP) dan nilai filter.
   - Menampilkan pasien yang sesuai dengan kriteria filter dalam bentuk tabel.
   - Jika tidak ada pasien yang sesuai, menampilkan pesan bahwa tidak ada pasien yang sesuai dengan kriteria filter.

5. **Perbarui Pasien (UPDATE)**
   - Pengguna memilih opsi "4" dari menu utama.
   - Fungsi `perbarui_pasien()` meminta input ID pasien yang akan diperbarui.
   - Meminta input data baru untuk pasien (nama, umur, keluhan, nomor HP) dan memperbarui data pasien yang sesuai dengan ID yang dimasukkan.
   - Jika data berhasil diperbarui, menampilkan pesan konfirmasi.
   - Jika ID pasien tidak ditemukan, menampilkan pesan kesalahan.

6. **Hapus Pasien (DELETE)**
   - Pengguna memilih opsi "5" dari menu utama.
   - Fungsi `hapus_pasien()` meminta input ID pasien yang akan dihapus.
   - Menghapus pasien dari `data_pasien` yang sesuai dengan ID yang dimasukkan.
   - Menampilkan pesan konfirmasi setelah pasien berhasil dihapus.

7. **Keluar dari Program**
   - Pengguna memilih opsi "6" dari menu utama untuk keluar dari program.
   - Program berakhir dengan menampilkan pesan "Keluar dari program."

## Kegunaan Blok Kode

1. **List `data_pasien`**
   - Menyimpan data pasien dalam bentuk list dari dictionary.

2. **Fungsi `tambah_pasien()`**
   - Menambah data pasien baru ke dalam list `data_pasien`.

3. **Fungsi `tampilkan_pasien()`**
   - Menampilkan semua data pasien dalam format tabel.

4. **Fungsi `perbarui_pasien()`**
   - Memperbarui data pasien berdasarkan ID yang dimasukkan oleh pengguna.

5. **Fungsi `hapus_pasien()`**
   - Menghapus data pasien berdasarkan ID yang dimasukkan oleh pengguna.

6. **Fungsi `filter_pasien()`**
   - Memfilter dan menampilkan data pasien berdasarkan kriteria yang dimasukkan oleh pengguna.

7. **Fungsi `main()`**
   - Menampilkan menu utama dan menangani input pengguna untuk menjalankan fungsi yang sesuai berdasarkan pilihan menu.

Dengan alur dan kegunaan blok kode tersebut, program ini memberikan solusi yang terstruktur dan mudah digunakan untuk mengelola data pasien.
