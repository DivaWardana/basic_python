#Contoh sederhana pembuatan list pada bahasa pemrograman python
list1 = ['kimia', 'fisika', 1993, 2017]
list2 = [1, 2, 3, 4, 5 ]
list3 = ["a", "b", "c", "d"]


#Cara mengakses nilai di dalam list Python
print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])

#Contoh update nilai dalam list python
list1[2] = 2001
print ("Nilai baru ada pada index 2 : ", list1[2])


#Contoh cara menghapus nilai pada list python
del list1[2]
print ("Setelah dihapus nilai pada index 2 : ", list1)