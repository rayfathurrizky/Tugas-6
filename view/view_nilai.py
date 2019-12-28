from model.daftar_nilai import data

def header():
    print("")
    print("PROGRAM INPUT NILAI")
    print("===================")
    print("")

def notoption():
    print(" Pilih opsi yang ada ")


def cetak():
    print("|=========================================================================|")
    print("|                          DAFTAR DATA MAHASISWA                          |")
    print("|=========================================================================|")
    print("| NO |      NAMA       |       NIM        | TUGAS |  UTS  |  UAS  | AKHIR |")
    print("|=========================================================================|")
    no = 1
    for tabel in data.values():
        print("|{0:3} | {1:15} | {2:16} | {3:5} | {4:5} | {5:5} | {6:5} |"
              .format(no, tabel[0], tabel[1], tabel[2], tabel[3], tabel[4], tabel[5]))
        no += 1
    print("|=========================================================================|")
    print("")


def nyari():
    from view.input_nilai import cari
    cari()