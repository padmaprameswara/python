data_nama = "Bambang"
data_umur = 16
data_tinggi = 165.5
data_ukuran_sepatu = 42

# string standar
data_string = f" nama = {data_nama}, umur = {data_umur},tinggi badan = {data_tinggi}, ukuran sepatu = {data_ukuran_sepatu}"
print(5*"="+"Data String"+5*"=")
print(data_string)

# sting multiline
data_string = f" nama = {data_nama}, \n umur = {data_umur},\n tinggi badan = {data_tinggi}, \n ukuran sepatu = {data_ukuran_sepatu}"
print("\n",5*"="+"Data String"+5*"=")
print(data_string)

# string multiline (kutip triplets)
data_string = f"""
nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
"""
print("\n",5*"="+"Data String"+5*"=")
print(data_string)

# mengatur lebar
data_string = f"""
nama = {data_nama:>3}
umur = {data_umur}
tinggi = {data_tinggi}
"""
print("\n",5*"="+"Data String"+5*"=")
print(data_string)