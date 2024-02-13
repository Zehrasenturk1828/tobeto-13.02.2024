# 1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("lütfen boyunuzu giriniz"))
agirlik = float(input("lütfen ağırlık giriniz"))

vki = float(agirlik / (boy * boy))
print("vücut kitle indeksiniz: ",vki)

# 2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("maaşınızı girin"))
zamOrani = float(input("zam oranınızı girin"))

zamliOran = float(maas * zamOrani / 100 + maas)
print("zamlı maaşınız: ",zamliOran)

# 3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
birinciSayi = int(input("birinci sayiyi girin"))
ikinciSayi = int(input("ikinci sayiyi girin"))
ucuncuSayi = int(input("ucuncu sayiyi girin"))

maximum = max(birinciSayi, ikinciSayi, ucuncuSayi)
print("en büyük değer", maximum)

# 4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)
daireYaricapi = float(input("yarıçapı giriniz"))
pi = 3.14
daireAlan = pi * daireYaricapi * daireYaricapi
daireCevre = 2 * (pi * daireYaricapi)

print("dairenin alanı: ",daireAlan , "dairenin çevresi: ", daireCevre)

# 5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
metin = input('Metni Girin : ')
ters = metin[::-1]

print('Girilen metnin tersi = %s' % (ters))
if ters == metin:
    print('Girilen metin palindrom')
else:
    print('Girilen metin palindrom değil.')