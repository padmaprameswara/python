# latihan

# kalkulator sederhana
print (10*"=")
print ("kalkulator sederhana")
print (10*"="+"\n")

angka_1= float (input ("masukan angka ="))
operator = input ("masukan operator bilangan (+,-,*,/) :")
angka_2 = float (input("masukan angka berikutnya ="))

# percabangan
if operator == "+":
    hasil = angka_1 + angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "-":
    hasil = angka_1-angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "/":
    hasil = angka_1/angka_2
    print (f"hasilnya adalah {hasil}")
elif operator == "*":
    hasil = angka_1*angka_2
    print (f"hasilnya adalah {hasil}")
else :
    print ("nominal penjumlahan dan perkalian tidak dapat dihitung")
print( "akhir dari program")
    