import time; # Digunakan untuk meng-import modul time
import calendar; # Digunakan untuk meng-import modul calendar

ticks = time.time()
print ("Berjalan sejak 12:00am, January 1, 1970:", ticks)

# Mendapatkan waktu sekarang
localtime = time.localtime(time.time())
print("Waktu lokal saat ini :", localtime)

# Mendapatkan waktu berformat
localtime2 = time.asctime( time.localtime(time.time()) )
print("Waktu lokal saat ini :", localtime2)

# Mendapatkan kalendar dalam sebulan
cal = calendar.month(2025, 3)
print("Dibawah ini adalah kalender:" )
print(cal)