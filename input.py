# input user
# data str
data_str = input ("masukan nama:")
print("data ini =", data_str,"type", type(data_str))

# casting input int
data_int =int (input("masukan nomor : "))
print ("data type", data_int ,type(data_int))

# input data float

number = float (input ("masukan nilai float :"))
print("data type :", number, type(number))

# bolean
biner = bool(int(input ('input data bool :'))) 
print ( 'data type ', biner ,type (biner))

# complex
data_complex = complex (input('input complex :'))
print("data type :", data_complex ,type(data_complex))

print ("Menghitung ruas segi panjang")
panjang = input (int("masukan nilai panjang"))
lebar = input (int("masukan nilai lebar"))
print (panjang * lebar)