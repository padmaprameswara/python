# Looping

# for
angka_list = [0,1,2,3,4,5] #angka list
print(angka_list)

for i in angka_list:
    print(f"i adalah -> {i}")
print ("end list loop\n")
angka_range = range (1,6)
for i in angka_range:
    print(f"i adalah -> {i}")
print ("end range loop\n")
angka_range2 = range (10)
for i in angka_range2:
    print(f'i adalah -> {i}')
print("end range 2\n")
angka_range3 = range (10) #range kalimat
for i in angka_range3:
    print('saya lapar')
print("end range 3\n")

# for dengan str
data_str = "saya mau makan"
for i in data_str:
    print (i)
print ("end loop str")


"""while"""
# while

angka = 1
while angka < 3:
    angka +=1
    print (f"angka sekarang ->{angka}")
    print("kamu di terima")
print('END')


# Nilai utbk lolos UNUD

unud =1
utbk_minimal=int(650)
for i in range (unud): 
    print("aku lolos pilihan 1")
print("aku lolos UNUD")

i = 610
while i< 650:
    i+=0
    print (f"aku lolos pilihan 2 ")
    if i > 1:
        break
print ("aku maba UNUD")