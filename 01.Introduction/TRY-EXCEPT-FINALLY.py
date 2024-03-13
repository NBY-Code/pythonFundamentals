# TRY -EXCEPT - FINALLY
try:
    x =int(input('bir tam sayı giriniz '))
    sonuc=x/0
    print(sonuc)
except ZeroDivisionError as err:# tek zero div erore bakar başka hiçbir errore bakma
    print(f"Bir tam sayı sıfıra bölünemez \n{err}")
   # print("Bir tam sayı sıfıra bölünemez")
finally:
    print("Ne olursa olsun çalışır")

try:
    #age = int(input('Age : ' ))
    #print(age)
    x=int(input("Tam sayi giriniz : "))
    sonuc=x/0
    print(sonuc)
except ValueError as err:
    print(f"{err}")
else:print("Exception çalışmazsa çalışır.")
finally:print("her zaman çalışırımm.")
