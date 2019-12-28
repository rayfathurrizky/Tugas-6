def inputan():
    from model.daftar_nilai import tambah_data
    while (True):
        nama = input("NAMA   : ")
        if nama == '':
            print('Nama tidak boleh kosong')
        else:
            break
    while (True):
        try:
            nim = int(input("NIM    : "))
            if nim == '':
                print('Masukan Nim dengan Angka')
        except ValueError:
            print('Masukan Nim dengan Angka')
        else:
            break
    while (True):
        try:
            tugas = int(input("TUGAS  : "))
            if tugas == '':
                print('Masukan TUGAS dengan Angka')
        except ValueError:
            print('Masukan TUGAS dengan Angka')
        else:
            break
    while (True):
        try:
            uts = int(input("UTS    : "))
            if uts == '':
                print('Masukan UTS dengan Angka')
        except ValueError:
            print('Masukan UTS dengan Angka')
        else:
            break
    while (True):
        try:
            uas = int(input("UAS    : "))
            if uas == '':
                print('Masukan UAS dengan Angka')
        except ValueError:
            print('Masukan UAS dengan Angka')
        else:
            break
    tambah_data(nama, nim, tugas, uts, uas)


def edit():
    from model.daftar_nilai import edit_data
    edit_data(nama=input("Edit data : "))


def delete():
    from model.daftar_nilai import delete_data
    delete_data(nama=input("Masukan Data : "))

def cari():
    from model.daftar_nilai import cari_data
    cari_data(nama=input("Masukan Nama : "))