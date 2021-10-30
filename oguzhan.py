# -*- coding: utf-8 -*-
"""
Created on Sat Oct 30 22:32:16 2021

@author: PC
"""
"""
yazili1=float(input("1. Yazılı : "))
yazili2=float(input("2. Yazılı : "))
yazili3=float(input("3.Yazılı : "))
yazili1=(yazili1+yazili2+yazili3) / 3
print(yazili1)
"""
"""sayi=input('Bir Sayı Giriniz : ') #Dışarıdan her istenen değer bize string olarak gelir // yazı metni olarak gelir 60
if(int(sayi)%2==0): # önce sayi değişkeni string ten int e çevriliyor daha sonra sayının  sayısal değerinin modu alınıp  tek veya çift olduğuna bakılır
    print('Girilen Sayı Çift')
else:print('Girilen Sayı Tektir')"""

"""
int = - ve + tüm tam sayıların işlemleri için kullanılır genellikle Id tanımlaması üzerinde daha çok işlevselliği mevcuttur.
float= daha çok virgüllü sayılarla işlem yapmak için kullanılır.
double= CBS harita veya koordinate sistemleri ve virgülden sonra 8 haneli sayılarla ilgilenenler içindir 
string= text metini yazı yazabildiğimiz metinlerdir a="Ali ayşeyi seviyor:)"
char = karekter tanımlaması için kullanılır kullanım şekli  a='B' b='c' tarzında tek bir karekter tanımlayabilirsin. 
"""
"""
if eğer
elif eğer değilse
else değilse 
"""
"""
sayi=input("Bir sayı giriniz : ")
if(int(sayi)>0):
    print(sayi+ " Sayısı pozitif sayıdır")
elif (int(sayi)<0):
    print(sayi+ " Sayısı negatif sayıdır")
elif (int(sayi)==0):
    print(sayi+ " Sayısı nötr sayıdır")
else:
    print("Yanlış işlem yaptınız")
"""
"""
yas=input("Yaşınızı Giriniz : ")
if (int(yas)>17):
    print("Ehliyet Alabilir")
else:
    print("Ehliyet Alamaz")
"""
"""
for
while
do while
foreach
"""
"""for i in range(1,20):
    if i%2!=0:
        print(i)"""
"""for i in range(1,101):
    if i%3==0 and i%5==0:
        print(i)"""
"""
metin = input("Metin giriniz : ")
sayac=0

while sayac<len(metin):
    print(metin[sayac])
    sayac+=1
"""
"""
def dikdortgenAlan(genislik,yukseklik):
    alan=genislik*yukseklik
    print("Alan : ", alan)
    return alan
gen=float(input("Genişlik : "))
yuk=float(input("Yükseklik : "))

dikdortgenAlan(gen,yuk)5
"""