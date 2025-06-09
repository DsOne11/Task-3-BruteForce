# ZIP Password Bruteforcer

Sebuah alat Python untuk melakukan brute force pada file ZIP yang dilindungi password menggunakan wordlist.

## Fitur

- Mendukung file ZIP yang dilindungi password
- Menggunakan wordlist untuk mencoba password
- Menampilkan progress bar dan informasi waktu
- Menangani error dengan baik
- Mendukung password dalam format UTF-8

## Instalasi

1. Pastikan Python 3.x sudah terinstal di komputer Anda
2. Instal dependensi yang diperlukan:
bash
pip install -r requirements.txt


## Cara Penggunaan

bash
python zip_bruteforce.py <file_zip> <wordlist>


### Argumen:
- file_zip: Path ke file ZIP yang dilindungi password
- wordlist: Path ke file wordlist yang berisi daftar password yang akan dicoba

### Contoh:
bash
python zip_bruteforce.py rahasia.zip passwords.txt


## Catatan

- Alat ini akan mencoba setiap password dari wordlist sampai menemukan password yang benar
- Progress ditampilkan dengan progress bar
- Waktu yang dibutuhkan akan ditampilkan ketika password ditemukan atau ketika semua password sudah dicoba
- Pastikan wordlist Anda diformat dengan benar (satu password per baris)

## Peringatan

Alat ini hanya untuk tujuan pendidikan dan tantangan CTF. Pastikan Anda memiliki izin untuk menguji keamanan sistem atau file apapun.
