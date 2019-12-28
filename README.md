# Tugas-6
Membuat Package dan modul



**Package & Module**

Module

• Modul merupakan bagian dari program yang berisi fungsi-fungsi yang dibuat pada file terpisah.

• Dengan adanya modul-modul yang terpisah, dapat dikelompokkan sesuai dengan fungsinya dan memudahkan dalam mengelola kode program.

• Modul dapat dipanggil sesuai dengan kebutuhannya.


**Membuat Module**

Untuk membuat modul pada Python cukup mudah.

• Buat sebuah file kode program python (ekstensi .py)

• Buat fungsi pada file tersebut.

Contoh:
Filename: example.py



# Python Module example def add(a, b):
   """This program adds two    numbers and return the result"""
   result = a + b    return result 




**Menggunakan Module**

• Untuk menggunakan modul yang telah dibuat cukup menggunakan perintah import
Contoh:
Import with renaming
>>> import example
>>> example.add(4,5.5)
9.5  # import module by renaming it
import math as m
print("The value of pi is", m.pi)


**Package**

• Package merupakan namespace yang berisi banyak modul dan paket.

• Package merupakan sebuah direktory yang berisi banyak file-file modul.

• Setiap package pada Python, harus ada file khusus yang bernama 
__init__.py

• File tersebut merupakan file kosong, atau bisa juga diisi dengan sesuatu.


**Membuat Package**

Untuk membuat package pada Python cukup mudah.

• Buat sebuah directory (folder), dan tambahkan file kosong dengan nama __init__.py

• Buat sejumah file kode program python (ekstensi .py) pada folder tersebut yang berisi fungsi-fungsi (modul program)
 

**Menggunakan Package**

• Untuk menggunakan package yang telah dibuat cukup menggunakan perintah import
import nama_package.nama_module atau from nama_package import nama_module



_**Penjelasan Program**_

1. Pertama kita tekan _**L**_ untuk melihat daftar nilai, lalu untuk menambahkan data kita tekan _**T**_ dan bisa dilihat seperti gambar dibawah ini.
![Screenshot (69)](https://user-images.githubusercontent.com/56881488/71545545-f50cc000-29be-11ea-9dc9-46a926137175.png)

2. Kedua kita tekan _**T**_ apabila ingin menambah data lagi misalkan kita tambah data cintakuuu dan tekan _**L**_ untuk melihatnya seperti gambar dibawah ini.
![Screenshot (70)](https://user-images.githubusercontent.com/56881488/71545546-f5a55680-29be-11ea-8e69-2aabfb69858b.png)

3. Ketiga kita tekan _**U**_ untuk mengubah data misalkan kita ubah data ray dan untuk melihatnya tekan _**L**_ seperti gambar dibawah ini.
![Screenshot (71)](https://user-images.githubusercontent.com/56881488/71545547-f5a55680-29be-11ea-8405-f31e21880be6.png)

4. Keempat kita tekan _**C**_ untuk mencari data misalkan kita cari data ray seperti gambar dibawah ini.
![Screenshot (72)](https://user-images.githubusercontent.com/56881488/71545549-fb9b3780-29be-11ea-9fb7-bca5561960d1.png)

5. Kelima kita tekan _**H**_ untuk menghapus data misalkan kita hapus data cintakuuu dan kita tekan _**L**_ untuk melihatnya dan untuk keluar program kita tekan _**K**_ seperti gambar dibawah ini.
![Screenshot (74)](https://user-images.githubusercontent.com/56881488/71545550-fc33ce00-29be-11ea-84eb-470b8a32caee.png)
