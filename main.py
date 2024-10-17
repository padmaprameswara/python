#Variable_bab 1
a = 10
b = 30
x = 2
y = 4
print ("nilai a =",a )
print ("nilai b =",b )
print ("nilai x =",x )
print ("nilai y =", y)

#nilai kedua

a=12
b=25
x=a
y=b
print ("nilai a =", x)
print ("nilai b =",y )\
    
    
    
# Buat list untuk menampung nama-nama teman
my_friends = ["Anggun", "Dian", "Agung", "Adi", "Adam"]

# Tampilkan isi list my_friends dengan nomer indeks 3
print (f"Isi my_friends indeks ke-3 adalah:{my_friends[3]}")

# Tampilkan semua daftar teman
print ("Semua teman: ada 5 orang".format(len(my_friends)))
for friend in my_friends:
    print (friend)
print("jangan belajar ini dlu ya komang kalau gak belajar dasar format")

print ("Menghitung ruas segi panjang")
panjang = int (input("masukan panjang :"))
lebar = int (input("masukan lebar :"))
print (f"nilai dari ruas segi panjang ={panjang * lebar}")

n = int (input("masukan nilai rekursif :"))
count = 1
a="1"
def rekursif (n):
    if (n<=10):
        print (a)
    else :
        print (rekursif - 1)
print ("end rekursif")
   
