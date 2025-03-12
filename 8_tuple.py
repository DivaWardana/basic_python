#Contoh sederhana pembuatan tuple pada bahasa pemrograman python
tup1 = ('fisika', 'kimia', 1993, 2017)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"

#Cara mengakses nilai tuple
print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])

tup4 = (12, 34.56)
tup5 = ('abc', 'xyz')

# Aksi seperti dibawah ini tidak bisa dilakukan pada tuple python
# Karena memang nilai pada tuple python tidak bisa diubah
# tup4[0] = 100;
# Jadi, buatlah tuple baru sebagai berikut
tup6 = tup4 + tup5
print (tup6)

tup = ('fisika', 'kimia', 1993, 2017)
print(tup)
# hapus tuple dengan statement del
del tup
# lalu buat kembali tuple yang baru dengan elemen yang diinginkan
tup = ('Bahasa', 'Literasi', 2020)
print("Setelah menghapus tuple :", tup)