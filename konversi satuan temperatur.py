# Konversi celcius ke satuan lain

print('\nROGRAM KONVERSI TEMPERATUR\n')
# satian celcius
celcius =float (input ('masukan suhu dalam celcius :'))

print("suhu berada kisaran", celcius,"C")

# reamur (4/5c)
reamur = (4/5)*celcius
print("suhu reamur berada kisaran",reamur,"R")


# fahrenheit (9/5c +32)
fahrenheit = (9/5) *celcius + 32
print("suhu fahrenheit berada kisaran",fahrenheit,"F")


# kelvin(CELCIUS +273)
kelvin = celcius + 273
print("suhu kelvin berada kisaran",kelvin,"K")


# satuan reamur

reamur =float (input ('masukan suhu dalam reamur :'))

print("suhu berada kisaran", reamur,"R")

# remaur-celcius(5/4r)
celcius= (5/4)*reamur
print("suhu celcius berada kisaran", celcius,"C")

# remaur-fahrenheit (9/4r+32)
fahrenheit=(9/5)*reamur+32
print("suhu fahrenheit berada kisaran", fahrenheit,"F")


# remaur-kelvin (5/4k +273))
kelvin=(5/4)*reamur +273
print("suhu kelvin berada kisaran", kelvin,"K")


# satuan fahrenheit

fahrenheit =float (input ('masukan suhu dalam fahrenheit :'))

print("suhu berada kisaran", fahrenheit,"F")

# fahrenheit-celcius (5/9 (f-32))
celcius = 5/9*(fahrenheit-32)
print("suhu celcius berada kisaran", celcius,"C")\


# fahrenheit-reamur(4/9 (f-32))
reamur = 4/9*(fahrenheit-32)
print("suhu reamur berada kisaran", reamur,"R")

# fahrenheit-kelvin(5/9 (f+459.67)
kelvin = 5/9*(fahrenheit+459.67)
print("suhu kelvin berada kisaran", kelvin,"K")


# satuan kelvin
kelvin =float (input ('masukan suhu dalam kelvin :'))

print("suhu berada kisaran", kelvin,"K")

#kelvin-celcius (k-273)
celcius= kelvin-273
print("suhu celcius berada kisaran", celcius,"C")


#kelvin-reamur 4/5(k-273)
reamur= 4/5*(kelvin-273)
print("suhu reamur berada kisaran", reamur,"R")


#kelvin-fahrenheit 9/5(K-459.67)
fahrenheit= (9/5*kelvin)-459.67
print("suhu fahrenheit berada kisaran", fahrenheit,"F")





