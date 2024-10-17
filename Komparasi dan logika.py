# latihan logika dan komparasi


# gabungan area rentang dari angka


# ++++++3-------10++++

inputUser = float(input ('masukan angka yang bernilai \n  kurang dari 3 \n atau lebih dari 10:\n'))
# <3
# check angka < 3
isKurangDari = (inputUser<3)
print("kurang dari 3:",isKurangDari)

# >10
isLebihDari = (inputUser>10)
print ("lebih dari 10 :",isLebihDari)

# ++++++3-------10+++++
isCorrect = isKurangDari or isLebihDari
print("angka yang dimasukan :", isCorrect)

print('\n',10*'=','\n')
# ------3+++++++10-----
inputUser = int (input ("masukan angka yang bernilai \n  lebih dari 3 \n dan kurang dari 10:\n"))
isLebihDari=inputUser >3
print ("Lebih dari 3",isLebihDari)

#+++++10----- 
isKurangDari=inputUser<10
print('Kurang dari 10 =', isKurangDari)

# -----3 +++++ 10------
isCorrect = isKurangDari and isLebihDari
print("angka yang dimasukan :", isCorrect)

# test uji coba

print('\n',10*'=','\n')
# 1)------0++++++5--------8+++++++11------
inputUser= int (input("masukan angka \n> 0 dan <5\n atau\n >8 dan < 11 :"))
# >0
isLebihDari=inputUser>0
print("lebih dari 0 =",isLebihDari)
# <5
isKurangDari=inputUser<5
print('kurang dari 5 =',isKurangDari)

# >8
isLebihDari=inputUser>8
print('lebih dari 8 =',isLebihDari)
# <11
isKurangDari=inputUser<11
print('kurang dari 11 =',isKurangDari)

isCorrect = isKurangDari and isLebihDari
print("angka yang dimasukan :", isCorrect)

# 2)+++++++0----------5++++++++8-------11+++++
print('\n',10*'=','\n')

inputUser= int (input("masukan angka \n> <0 atau > 5\n<8 atau >11:"))
# <0
isLebihDari=inputUser<0
print("lebih dari 0 =",isLebihDari)
# >5
isKurangDari=inputUser>5
print('kurang dari 5 =',isKurangDari)

# <8
isLebihDari=inputUser<8
print('lebih dari 8 =',isLebihDari)
# >11
isKurangDari=inputUser>11
print('kurang dari 11 =',isKurangDari)

isCorrect = isKurangDari or isLebihDari
print("angka yang dimasukan :", isCorrect)