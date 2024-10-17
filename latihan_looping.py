# latihan looping
sisi = 10

# for
# dummy variable
count =1 
for i in range (sisi):
    print ("*"*count)
    count+=1
print ("end for")

# while
count =1
while True:
    print ("*"*count)
    count+=1
    if count > sisi :
        break
print ("end while")

# contoh 3 hanya ganjil
count =1
spasi =5
while True:
    if (count%2) : 
        #print jika ganjil
        print ("*"*count)
        count+=1
        
       
    #akan kembali ke atas jika ganjil
    else :
        count+=1
        continue
    #akan break jika count melebihi variable
    if count > sisi :
        break
print ("end while 2")

# contoh 4 hanya genap
count =1
while True:
    if (count%2) : 
    #print jika genap
        count+=1
      
        continue
        
    #akan kembali ke atas jika ganjil
    else :
        print ("*"*count)
        count+=1
       
    #akan break jika count melebihi variable
    if count > sisi :
        break
print ("end while 3")
# contoh 5 segitia hanya genap
count =1
spasi = int (5)
while True:
    if (count%2) : 
        #print jika genap
        spasi -=1
        count+=1
        continue
        
    #akan kembali ke atas jika ganjil
    else :
        print (" "*spasi,"+"*count)
        sisi -=1
        count+=1
    #akan break jika count melebihi variable
    if count > sisi :
        break
print ("end while 4")

# contoh 6 segitiga hanya ganjil
count =1
spasi =5
while True:

    if (count%2) : 
        #print jika ganjil
        print (" "*spasi,"+"*count)
        spasi-=1
        count+=1
       
    #akan kembali ke atas jika ganjil
    else :
        count+=1
        continue
    #akan break jika count melebihi variable
    if count > sisi :
        break
print ("end while 5\n")

sisi = int (input("masukan pola"))
count=1
for i in range (sisi):
    print ("*"*count)
    count+=1
print ("end")


a = int (input("masukan angka"))
count=1
deklarasi = "Hai Guys"
kontradiks = "Lahh Bego"
while True:
    if (a <= 12):{
        print(deklarasi)
        
    }
    else:
        print(kontradiks)
    if a > count:
        break
    
print ("end")