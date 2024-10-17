# date and time (latihan)
import datetime as dt

print("Silahkan Masukan Tanggal Lahir")
tanggal = int(input("tangal\t:"))
bulan = int(input("bulan\t:"))
tahun = int(input("tahun\t:"))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print(f"Tanggal lahir anda adalah {tanggal_lahir}")
print(f"Hari lahir anda adalah {tanggal_lahir :%A}")

hari_ini = dt.date.today()
print(f" hari ini tanggal {hari_ini}")
umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days//365
umur_bulan = (umur_hari.days%365)//30
print(f"umur anda adalah : {umur_hari}")
print(f"umur anda adalah : {umur_tahun}, {umur_bulan}")

