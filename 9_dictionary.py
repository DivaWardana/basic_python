#Contoh cara membuat Dictionary pada Python
dict = {'Name': 'Diva', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])

#Update dictionary python
dict['Age'] = 8; # Mengubah entri yang sudah ada
dict['School'] = "Trilogi School" # Menambah entri baru
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])

#Contoh cara menghapus pada Dictionary Python
del dict['Name'] # hapus entri dengan key 'Name'
dict.clear() # hapus semua entri di dict
del dict # hapus dictionary yang sudah ada
print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])