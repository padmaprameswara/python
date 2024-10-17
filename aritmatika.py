# aritmatika

a=5
b=3

# OPERASI TAMBAH

hasil = a+b
print (a,"+",b,'=', hasil)

# OPERASI pengurangan (-)

hasil = a-b
print (a,"-",b,'=', hasil)

# OPERASI pembagian (:)

hasil = a/b
print (a,":",b,'=', hasil)
# OPERASI perkalian (*)

hasil = a*b
print (a,"x",b,'=', hasil)


# OPERASI EKSPONEN(**)

hasil = a**b
print (a,"pangkat",b,'=', hasil)

# OPERASI modulus(%)

hasil = a%b
print (a,"%",b,'= sisa :', hasil)


# OPERASI floor division(//)

hasil = a//b
print (a,"//",b,'= dibulatkan:', hasil)

'''
    1.kurung()
    2.eksponen (pangkat)
    3.operasi hitung
'''
# PRIORITAS OPERASI, operational precedence

x=3
y=4
z=5

hasil = x ** y * z / x // y % x + z + x - y

print (x,'**',y,'*',z,'/',x,'//',y,'%',x,'+',z,'+',x,'-', y,"=", hasil)

hasil = x ** y // 9
print ("hasil =", hasil  )

# tanda kurung
hasil =(x * z + 2) / y**2

print('(',x, '*', z ,'+', 2,')' ,'/', y,'**',2,"hasil =", hasil)