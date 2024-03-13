#While Loops
# Tekrarlı işlemler için kullanılır içerisinde koşul barındırır koşula göre işlemler tekrar eder.
#region Soru 1
#Kullanıcıdan bir sayı alın ve bu sayıya kadar olan sayıların toplamını bulun.
# sayi=int(input("Lütfen bir sayi giriniz : "))
# toplam=0
# sayac=0
# while sayi>=sayac:
#     toplam+=sayac
#     sayac+=1
# print(toplam)
#endregion
#region Soru 2
#Kullanıcıdan bir sayı alın ve bu sayıya kadar olan tek ve cift sayıların toplamını bulun.
# sayi=int(input("Lütfen bir sayi giriniz : "))
# tek_Toplam=0
# cift_Toplam=0
# sayac=0
# while sayi>=sayac:
#     if sayac%2==1:
#         tek_Toplam+=sayac
#     else:cift_Toplam+=sayac
#     sayac+=1
# print(f"Tek sayıların toplamı = {tek_Toplam} \nÇift sayıların toplamı : {cift_Toplam}")
#endregion
#region Soru 3
#Kullanıcıdan bir sayı alın ve bu sayı kadar yıldız (*) kullanarak bir üçgen deseni oluşturun.
# sayi = int(input("Bir sayı girin: "))
# sayac = 1
# while sayac <= sayi:
#     print("*" * sayac)
#     sayac += 1

#endregion
#region Soru 4
#Bir listenin elemanlarını yazdırın .
# liste=[1,2,3,4,5,6,7,8,9]
# for eleman in liste:
#     print(eleman ,end=" ")
#endregion
#region Soru 5
# Belirli aralıktaki sayıları ekrana yazdırın.
# for i in range(1,16):
#     print(i , end=" ")
#endregion
#region Soru 6
# Kullanıcıdan alınan metindeki harfleri boşluk bırakrak yazrıdın.
# metin = input("Lütfen bir metin giriniz : ")
# for i in  metin:
#     print(i , end=" ")
#endregion
#region Soru 7
# Kullanıcıdan alınan metindeki kelime sayısnı bulma .
# metin = input("Lütfen bir metin giriniz : ")
# kelime_sayisi=0
# for i in  metin.split():
#     kelime_sayisi+=1
# print(f"{metin} metnindeki kelime sayısı = {kelime_sayisi}")
#endregion
