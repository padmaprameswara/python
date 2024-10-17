# setiap hasil = boolean

# >,<,>=,<=,==,!=, is, isn't

# >
a=3 
b=12

hasil = a>b
print(a,'>',b,"=", hasil)

# <
hasil = 10<b
print(10,"<",b,"=", hasil)


# <=
hasil = a<=b
print (a,"<=",b,"=", hasil)

# >=
hasil = a>=b
print (a,">=",b,"=", hasil)

# ==
hasil = a==3
print(a,"==", 3 ,"=", hasil)

hasil = a==4
print(a,"==", 4 ,"=", hasil)

# !=
hasil = a!=3
print(a,"!=", 3 ,"=", hasil)
hasil = a!=4
print(a,"!=", 4 ,"=", hasil)


print ("object identity (is)================")

x=4 #assignment membuat object
y=3
print('nilai x =',x, "id =",hex(id(x)) )
print('nilai y =',y, "id =",hex(id(y)) )
hasil = x is y
print("x is y =", hasil)


x=4 #assignment membuat object
y=3
print('nilai x =',x, "id =",hex(id(x)) )
print('nilai y =',y, "id =",hex(id(y)) )
hasil = x is not y
print("x is not y =", hasil)