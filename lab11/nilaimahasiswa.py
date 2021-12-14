# praktikum


nilaimahasiswa = []

# tambah data mahsiswa
def tambah(nama, nilai):
    nilaimahasiswa.append({
        'nama': nama,
        'nilai': nilai
    })


# tampilkan data mahasiswa
def tampilkan():
    for item in nilaimahasiswa:
        print(item['nama'], item['nilai'])


# menghapus data mahasiswa
def hapus():
    list = ["dooshik 90", "isaac 85", "yeonjun 75"]
    list.remove("isaac 85")
    print (list)


# mengubah data mahasiswa
def ubah():
    name = ["dooshik 90", "isaac 85", "yeonjun 75"]
    name[1] = "san 100"
    print (name)



