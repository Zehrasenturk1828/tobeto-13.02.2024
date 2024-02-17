#1- İlk iki elemanı 1'e eşit olan, en az 20 elemanlı bir fibonacci serisini liste halinde oluşturan döngü yazalım.

fibonacci = [1, 1]
while len(fibonacci) < 20:
    fibonacci.append(fibonacci[-1] + fibonacci[-2])

print(fibonacci) 

#2- Kullanıcıdan aldığı sayının mükemmel olup olmadığını söyleyen bir program yazınız.(Arş. Mükemmel sayı?)

sayi = int(input("Sayi Giriniz:"))
toplam=0
 
for i in range(1,sayi):
    if(sayi%i == 0):
        toplam +=i
        
if(sayi == toplam):
    print("Mükemmel Sayidir.")
else:
    print("Mükemmel Sayi Degildir")

#3- Kullanıcıdan girilen sayının EBOB ve EKOK'unu bulan programı yazınız.

birinciSayi = int(input("Birinci Sayıyı Giriniz : "))
ikinciSayi = int(input("İkinci Sayıyı Giriniz : "))
 
if (birinciSayi > ikinciSayi):
    kucuksayi = ikinciSayi
else:
    kucuksayi = birinciSayi
for i in range(1,kucuksayi+1):
    if (birinciSayi % i==0) and (ikinciSayi%i ==0):
        ebob = i
        ekok = (birinciSayi*ikinciSayi)//ebob # // -> kalansız bölme

print ("EBOB:", ebob)
print ("EKOK:", ekok)

#4- Kullanıcıdan girilen sayının asal sayı olup olmadığını söyleyen bir program yazınız.

sayi = int(input("Lütfen sayı giriniz: "))
if sayi > 1:
   
    for i in range(2,sayi):
        if (sayi % i) == 0:
            print(sayi," asal sayı değildir.")
            break
    else:
        print(sayi," asal sayıdır.")
 
else:
    print(sayi," asal sayı değildir.")

#5- Kullanıcıdan girilen sayının asal çarpanlarını bulan bir program yazınız. 

sayi = int(input("Lütfen sayı giriniz: "))
factor = 2
print(sayi, "sayısının asal çarpanları:")
while factor <= sayi:
    if sayi % factor == 0:
        print(factor)
        sayi //= factor
    else:
        factor += 1