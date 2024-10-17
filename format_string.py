name = "nando"
str = "hello" +name+ "apa kabar"
print (str)

nama ="dendi"
format_str = f"the legend of dota 2 {nama}"
print(format_str)

# angka
angka = 2024.6
format_str = f"angka = {angka}"
print(format_str)

# boolean
bool = True
format_str= f"boolean = {bool}"
print(format_str)

# bilangan bulat
nomor = 11
format_str= f"bilangan bulat = {nomor:d}"
print(format_str)

# bilangan ordo ribuan
no = 200000
format_str=f"ribuan {angka:,}"
print(format_str)

# bilangan desimal
angka = 3000300
format_str =f"desimal {angka:.3f}"
print(format_str)

# leading zero
angka = 3000300
format_str =f"leading zero {angka:012.3f}"
print(format_str)

#tanda +_
min_x = -12
plus_y = 6
format_minus = f"minus = {min_x:+d}"
format_plus = f"plus ={plus_y:+d}"

print(format_plus)
print(format_minus)

# persen
persentase = 00.3334
format_persen =f"persentase = {persentase:%}"
print(format_persen)

# oprasi aritmatika
uang=1000
nilai = 3
format_str = f"harga total ={uang*nilai:,}"

print(format_str)

# format angka lain (binary, octal, hexadecimal)
angka = 223
format_binary =f"binary ={bin(angka)}"
format_octal =f"octal ={oct(angka)}"
format_hex =f"hex ={hex(angka)}"
print (format_binary)
print (format_octal)
print (format_hex)