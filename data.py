#data integer (satuan)
data_integer= 1
print("data:",data_integer,"bertipe:",type (data_integer))
print("bertipe:", type(data_integer))

#data float (angka koma)
data_float = 1.2
print("data :", type(data_float))

#data string (kumpulan karakter)

data_string = "ucup"
print("data ini bertipe :", data_string ,type(data_string))

#data bolean (biner true/false)
data_bool = True
print("data ini bertipe :", data_bool ,type(data_bool))


#data khusus (complex)
data_complex= complex(5,9)
print("data ini bertipe :",data_complex ,type(data_complex))

#tipe data dari bahasa C

from ctypes import c_long, c_double

data_c_double = c_double (1.2)
print("data ini :", type(data_c_double))