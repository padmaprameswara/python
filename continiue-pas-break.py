# pass-> berfungsi sebagai dummy, tidak akan dieksekusi
# pass
angka =0
while angka < 5:
    angka +=1
    if angka == 3 :
        pass
        
    print (angka)

# continue
angka =1
print (f"angka sekarang -> {angka}")

while angka < 5 :
    angka += 1 
    print(f"angka sekarang -> {angka}")
    if angka == 2 :
        print ("Hallo")
        continue #akan membuat loop meloncatt ke berikutnya
    print ("Menyala")
print ("nice")

# break
angka = 0
while angka < 6:
    angka+=1
    print(f"angka sekarang ->{angka}")
    if angka == 3:
        print ("2025 ITS")
        break
    print("lets begin")
print ("END")

# contoh 2
data_int = int(input("masukan nominal angka"))
angka = 0
while True:
    angka+=1
    print(f"count angka ->{angka}")
    if angka == data_int:
        print ("2025 ITS")
        break
    print("lets begin")
print ("END OF JOURNY")