# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from nilaimahasiswa import tambah, tampilkan, hapus, ubah


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'90, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print("====== DAFTAR NILAI MAHASISWA ======")
    tambah('dooshik', '90')
    tambah('isaac', '85')
    tambah('yeonjun', '70')
    tampilkan()
    print("====== SETELAH DIHAPUS ======")
    hapus()
    print("====== SETELAH DIUBAH ======")
    ubah()