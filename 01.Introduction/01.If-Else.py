#region Soru1
# Bir sayının pozitif, negatif veya sıfır olduğunu kontrol etme.
# sayi=int(input("Lütfen bir sayi giriniz : "))
# if(sayi>0):
#     print("Sayi pozitiftir")
# elif(sayi==0):
#     print("Sayi sıfıra eşittir")
# else:print("Sayi Negatiftir")
#endregion
#region Soru2
# İki sayının eşit veya hangi sayı daha olup olmadığını kontrol etme.
# sayi_1=int(input("Lütfen bir sayi giriniz : "))
# sayi_2=int(input("Lütfen bir sayi giriniz : "))
# if(sayi_1==sayi_2):
#     print("Sayılar biribirine eşittir")
# elif(sayi_1>sayi_2):
#     print(f"{sayi_1} daha büyüktür")
# else:
#     print(f"{sayi_2} daha büyüktür")
#endregion
#region Soru3
# Bir sayının tek veya çift  olduğunu kontrol etme.
# sayi = int(input("Lütfen bir sayı giriniz : "))
# if(sayi%2==0):
#     print("Girilen sayı ÇİFTTİR")
# else:print("Girilen sayı TEKTİR")
#endregion
#region Soru4
# Üç sayı arasındaki en büyüğü bulma.
# sayi_1=int(input("Lütfen bir sayı giriniz : "))
# sayi_2=int(input("Lütfen bir sayı giriniz : "))
# sayi_3=int(input("Lütfen bir sayı giriniz : "))
# if(sayi_1>sayi_2 and sayi_1>sayi_3):
#     print(f"{sayi_1} en büyük sayıdır")
# elif(sayi_2>sayi_3):
#     print(f"{sayi_2} en büyük sayıdır")
# else:print(f"{sayi_3} en büyüktür . ")
#endregion
#region Soru5
# Üç sayı arasındaki en küçüğü bulma.
# sayi_1=int(input("Lütfen bir sayı giriniz : "))
# sayi_2=int(input("Lütfen bir sayı giriniz : "))
# sayi_3=int(input("Lütfen bir sayı giriniz : "))
# if(sayi_1<sayi_2 and sayi_1<sayi_3):
#      print(f"{sayi_1} en küçük sayıdır")
# elif(sayi_2<sayi_3):
#     print(f"{sayi_2} en küçük sayıdır")
# else:print(f"{sayi_3} en küçüktür . ")
#endregion
#region Soru6
#Verilen yılın artık yıl olup olmadığını kontrol etme.
# yil=int(input("Bir yıl giriniz : "))
# if(yil%4==0):
#     print(f"{yil} artık yıldır.")
# else:print(f"{yil} artık yıl değildir.")
#endregion
#region Soru7
# Verilen karakterin sesli harf mi mi olduğunu kontrol etme.
# karakter=input("Lütfen bir karakter giriniz : ")
# if(karakter=="a" or karakter=="e" or karakter=="i" or karakter=="ı"or karakter=="u" or karakter=="ü" or karakter=="o" or karakter=="ö"):
#     print(f"Girilen karakter sesli harftir .  ")
# else:print("Yanlış bir giriş yaptınız .")
#endregion
#region Soru8
# Bir sayının 3'e veya 5'e tam bölünüp bölünmediğini kontrol etme.
# sayi=int(input("Lütfen bir sayi giriniz : "))
# if(sayi%3==0 or sayi%5==0):
#     print(f"{sayi} sayısı 5  veya 3 tam bölünmektedir  .")
# else:print(f"{sayi} sayısı 3 veya 5 bölünemez . ")
#endregion
#region Soru9
# İki sayının toplamının 75'dan büyük olup olmadığını kontrol etme.
# sayi_1=int(input("Bir sayı giriniz . "))
# sayi_2=int(input("Bir sayı giriniz . "))
# toplam=sayi_1+sayi_2
# if(toplam>=75):
#     print("Girilen sayıların toplamı 75ten büyüktür.")
# else:
#     print("Girilen sayıların toplamı 75ten küçüktür.")
#endregion
#region Soru10
#Vize Final  Ortalaması 50 den küçük olan öğrenciler büte sokab tekrar 50 eden küçükse kaldı diyen program
# vize=int(input("Vize notunuzu giriniz : "))
# final=int(input("Final notunuzu giriniz : "))
# ortalama=(vize+final)/2
# if( 0<=vize<=100 and 0<=final<=100):
#     if(ortalama>=50 ):
#         print("Dersi Geçtiniz")
#     else:but=int(input("Büt notunuzu giriniz : "))
#     ortalama=(vize+but)/2
#     if(ortalama>=50):
#         print("Dersi Geçtiniz")
#     else:print("Dersten Kaldınız")
# else:print("Yanlış giriş yaptınız")
#endregion
