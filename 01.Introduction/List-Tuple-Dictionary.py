#Listeler, biden çok öğeyi depolamak için kullanılan değiştirilebilir ve sıralı veri yapılarıdır.
# meyveler=["elma","armut","çilek","muz"]
# print(meyveler[0])
# print(meyveler)
# for i in meyveler:
#     print(i, end="--")
# meyveler.append("karpuz")#=>son indexine karpuzu ekler
# print(meyveler)
# meyveler.insert(2,"kiraz")#ikinci indexe kiraz bilgisini ekler
# print(meyveler)
# meyveler.remove("armut")#=> armut bilgisini listeden siler
# print(meyveler)
# meyveler.pop(3)#=> 3üncü indexteki bilgiyi siler
# print(meyveler)
# sebzeler=["biber","patlıcan","salatalık","lahana"]
# sebzeler.extend(meyveler)#=> işki listeyi birbirine ekler

# ---------------------------------------------------------------------------------------------------------------
#List Comprehansion
#[expression for item in liste if condition]
#rakamların list comprehansion kullanarak ekrana yazdırın
# print(([item for item in range(10)]))
#
# power = [item *item for item in range(10)]
# print(power)
#
# print([i*i for i in range(100) if i % 3 ==0])

# ---------------------------------------------------------------------------------------------------------------
#Tuple'lar(Tuples) listelere çok benzerler ancak değiştirilemezler
renkler = ("kırmızı", "yeşil", "mavi")
print(renkler[0])
print(renkler[2])

# ---------------------------------------------------------------------------------------------------------------
#Dictionary'lar bir anahtar - değer çiftlerini ilişkilendiren veri yapılarıdır.
# Bir sözlük oluşturma
kisiler = {"ad": "Ali", "yas": 25, "sehir": "İstanbul"}
print(kisiler["ad"])
print(kisiler["yas"])

# ---------------------------------------------------------------------------------------------------------------
tuple_1 = ('Galatasaray' , 'Fenerbahçe', 'Beşiktaş', 'Tranzonspor')
tuple_2 = ('12' , '35.5', 'b', 'Eagles','Patrios','Red Skins')
tuple_3 = tuple_1+tuple_2
print(tuple_3)

# Dilimleme (Slicing)
print(tuple_3[0:3]) #output => ('Galatasaray' , 'Fenerbahçe', 'Beşiktaş')
print(tuple_3[2:4]) #output => ('Beşiktaş', 'Tranzonspor')
print(tuple_3[::2]) #output=> ('Gawlatasaray', 'Beşiktaş', '12','b','partios')
print(tuple_3[-1]) #output=> Red Skins
print(tuple_3[::-1]) #output => ('Red Skins', 'Patrios', 'Eagles', 'b', '35.5', '12', 'Tranzonspor', 'Beşiktaş', 'Fenerbahçe', 'Galatasaray')
print(tuple_3[::-2]) #output => (('Red Skins', 'Eagles', '35.5', 'Tranzonspor', 'Fenerbahçe'))
print(tuple_3[3::-2]) #output => (('Tranzonspor', 'Fenerbahçe'))

