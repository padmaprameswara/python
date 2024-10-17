# operasi logika atau boolean

#not , or , and , xor

# NOT
print('=====Not====')
a=True
b=not a
print('data a =',a)
print('----------- NOT')
print('data b =',b)


# OR (jika salah satu true maka hasilnya true)
print('===========OR========')
a=False
b=True
c= b or a
print(a,"OR",b,"=", c)
a=False
b=False
c= b or a
print(a,"OR",b,"=", c)
a=True
b=True
c=b or a
print(a,"OR",b,"=", c)
a=True
b=False
c= a or b
print(a,"OR",b,"=", c)


# and (jika salah satu nila False maka hasilnya False)
print('===========and========')
a=False
b=True
c= b and a
print(a,"and",b,"=", c)
a=False
b=False
c= b and a
print(a,"and",b,"=", c)
a=True
b=True
c=b and a
print(a,"and",b,"=", c)
a=True
b=False
c= a and b
print(a,"and",b,"=", c)

# xor (^) (akan true jika salah satu true sisanya false)
print('===========xor========')
a=False
b=True
c= b ^ a
print(a,"xor",b,"=", c)
a=False
b=False
c= b ^ a
print(a,"xor",b,"=", c)
a=True
b=True
c=b  ^a
print(a,"xor",b,"=", c)
a=True
b=False
c= a ^ b
print(a,"xor",b,"=", c)

z= 2
x=1
if( x>1):
    print("hari ini kelas tutorial")
else :{
    print("gak jadi kelas")
}