# menyambung string
nama_a = "pam"
nama_b = "ember"
nama_c= "spirit"

nama_lengkap = nama_a + nama_b + nama_c
print (nama_lengkap)

#menghitung panjang string
panjang = len (nama_lengkap)
print(panjang)

# operator sting
d = "a"
status = d in nama_lengkap
print("string "+d, ""+ "ada di"+"", nama_lengkap ,"=",str(status))


d = "p"
status = d not in nama_lengkap
print("sting ",d, ""+ "tidak ada di"+"", nama_lengkap ,"=",str(status))

# indexing
print("index ke-0 adalah ", nama_lengkap[0])
print("index ke-1 adalah ", nama_lengkap[1])

# item paling kecil
print("paling kecil :", min (nama_lengkap))
# item paling besar
print("paling besar :", max (nama_lengkap))

ascii_code = ord(" ")
print("ascci code untuk spasi adalah", str (ascii_code))
data = 111
print('char untuk ascci 111 adalah', chr(data))

# operator dalam metod

data = "void spirit"
jumlah = data.count("i")
print("jumlah i pada data adalah", str(jumlah))

# merubah case string
salam ="bro"
print ('normal =', salam)
salam = salam.upper()
print ('upper =', salam)
salam = salam.lower()
print ('lower =', salam)

#3 pengecekan dengan isX method
# case check
example = "Hai"
apakah_lower = example.islower()
print(example, "is lower =", str(apakah_lower))
apakah_lower = example.isupper()
print(example, "is upper =", str(apakah_lower))

# is alpha () <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek angka dan huruf
# isdecimal ()<-- untuk mengecek angka semua
# isspace()<-- mengecek spasi, tab , new line
# istittle() <-- untuk mengecek semua kata di awali huruf besar

judul ="Kuliah Mudah Menyenangkan"
cek_judul = judul.istitle()
print (judul,"is tittle =", cek_judul)

# check komponen startswith () endswith
check_start ="Ember Spirit".startswith("Ember ")
print("start =",check_start)
check_end ="Ember Spirit".endswith("Spirit")
print("end =",check_end)

## penggabungan komponen join() split ()
split = [ 'saya','adalah','mahasiswa']
gabung = ','.join(split)
print (gabung)
print(split)

gabung= ' '.join(split)
print (gabung)

gabung = 'saya-adalah-program'
print(gabung.split("-"))

# alokasi character rjust(), ljust(), center()
right= 'kanan'.rjust(20)
print ("'",right,"'")

left= 'kiri'.ljust(20)
print ("'",left,"'")
center= 'center'.center(20,"-")
print ("'",center,"'")

# kebalikannya -> stip()
center=center.strip ('-')
print ("'",center,"'")