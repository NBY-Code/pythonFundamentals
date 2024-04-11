#Abstraction (Soyutlama)
# Soyutlama ile amaçlana ana mantık şudur : ata sınıfları soyut yaparak alt sınıflara kural koymak.Bir başka değiş ile ata sınıf ile altsınıflar arasında kontrat yada sözleşme imzalıyoruz  .GErçek hayatta nasıl kontrol bozulmazsa yazılımda da bozulmaz.
#region Decorator
#Python programlama dilinde kullanılan bir keyword'tür. Bir fonksiyonu bir decoratör ile var olan yeteneği üzerine bir yetenek daha ekleyebiliriz.Methodlarımızı yoğun kod yazmadan yeni bir yetenek ile extend etmiş oluyoruz.Python'da built-in bir çok decoratör vardır. Bunlardan Bazıları @abstractmethod,@static,@property vb. tabi ki custom decoretör yazılabilinir.
# def uppercase_name(function):
#     def inner_func():
#         func = function()
#         make_uppercase=func.upper()
#         return make_uppercase
#     return inner_func()
# def full_name():
#     return 'mike tyson'
# #Call edilmedi sadece adı çağrıldı
#
# print(uppercase_name(full_name))
#
# @uppercase_name
# def get_name():
#     return 'burak yilmaz'
# #Call edilmedi sadece adı çağrıldı
# print(get_name)
#
# from time import sleep, time
#
# from math import pow, factorial
#
# def calculate_time_execute(func):
#     def inne_func(*args,**kwargs):
#         start_time=time()
#         #sleep(10)
#         func(*args,**kwargs)
#         finish_time=time()
#         print(f'===========\n'
#               f'Process Name : {func.__name__}\n'
#               f'Start Time : {start_time}\n'
#               f'Finish Time : {finish_time}')
#     return inne_func
#
# @calculate_time_execute
# def us_alma(a: int, b: int):
#     print(f'Sonuc : {pow(a, b)}')
#
# @calculate_time_execute
# def faktoriyel_hesaplama(number: int):
#     print(f'Sonuc : {factorial(number)}')
#
# @calculate_time_execute
# def toplama(x: int, y: int, z: int):
#     print(f'Sonuç : {x + y + z}')
#
# us_alma(2,5)
# faktoriyel_hesaplama(5)
# toplama(3,4,5)
# ÖDEVVVV ==>
# keni görevlerini execute ederken harcadıkları süreyide ekrana yazınız startime , end time fonksiyonu call edip
# 1- inner funtion argüman alıcak
# 2- sistemi sleeple uyutabilirsin bunu yapıcaksın
#endregion

#region metaclass
#Python'da metaclass , başka sınıfları yaratmak için kullanılan bir sınıftır. Bir sınıf kendi instance'nın nasıl davranacağını tanımlar,lakin metaclass bir sınıfın nasıl davrancağını tanımlar .Genellikle sınıf oluşturma davranışını özelleştirme ve sınıfın otomatik oalrak hangi özel fonksiyonlara sahip olacağını belirtmek için kullanıyoruz.
#endregion
#abc meta class
from abc import ABC,abstractmethod
class BaseMuzikAleti:
    def __init__(self,brand,model):
        self.model=model
        self.brand=brand

class Gitar(BaseMuzikAleti):
    def __init__(self, brand, model,tel):
        super().__init__(brand, model)
        self.tel=tel
class Keman(BaseMuzikAleti):
    def __init__(self, brand, model,kasa):
        super().__init__(brand, model)
        self.kasa=kasa

class Müzisyen:
    def __init__(self,first_name,last_name):
        self.last_name=last_name
        self.first_name=first_name
        self.caldigi_enstrumanlar = []

class BaseService(ABC):
    # Abstract bir sınıf içersinde herhangi bir methodu "@abstractmethod" decoratörü ile işaretlersem bu method soyut bir method artık soyut bir method olmuştur.
    # Abstract olarak işaretlenmiş bir fonksiyonun gövdesi olmaz yani ilgili fonksiyona bir business logic yüklenmez .Bu bağlamda aşağıdaki methodu "pass" diyerek ona gövde atamadık.
    # Neden absract metodlara göcde yazılmaz ?
    # Çünkü abstract olarak işaretlenmiş methodlar alt sınıflarda override edilmeye zorunludur.Bu zorunluluk dün konuştuğumuz kontrat mevzusudur.
    # Zaten aşağıdaki method alt sınıflarda override edilmeye zorunlu olduğu için gövde vermek mantıksızdır.
    @abstractmethod
    def call_sound(self) -> str: pass

    # Abstract sınıf içersinde abstract olmayan methodlar barındırılabilinir.Bu methodlar override edilmeye zorunlu değildir.Alt sınıfta ihtiyaca göre override edilirler yada edilmezler.
    def hello_everyone(self):
        print(' Hi ')

    # Burada tanımlanan soyut method alt sınıflarda değiştirlemez. yani bir var olan argümanlarına yenisi eklenemez yada argüman yoksada yeni bir argüman eklenmez.
    # Bu adeğiştirlemez özelliğini düşündüğümüzde aklımıza OCP(Open Closed Principle) yazılım prensibi gelmektedir.Bu prensip bize değşisime kapalı geliştirmeye açık sınıflar yaratmamızı salık verir.
    @abstractmethod
    def harmonize(self) -> str: pass


class GitarSevice(BaseService):
    def harmonize(self) -> str:
        return 'Akord edildi'

    def call_sound(self) -> str:
        return 'Gitar Sesi'

    # Alt sınfıların ihtiyaçlarına göre kendine has methodları olabilir.Lakin başka yaklaşımları bozmamak için genel olarak ortaya yazılarak override edilmesi tercih edilir.
    def salve(self):
        print("hhjkkjkg")


class KemanService(BaseService):

    def call_sound(self) -> str:
        return 'Keman Sesi'

    def harmonize(self) -> str:
        return 'Akord edildi'

    # Bu methodu ister override ederim istersem etmem çünkü ata sınıfta soyut olarak işaretlenmedi
    def hello_everyone(self):
        print('Kimseyi selamlamak istemiyorum')


def main():
    gitar_service = GitarSevice()
    keman_service = KemanService()

    gitar = Gitar('Fender', 'Classical Gitar', 'Kaliteli Tel')
    keman = Keman('Godrigez', 'Classical', 'Meşe')
    muzisyen = Müzisyen('Burak', 'Yılmaz')
    muzisyen.caldigi_enstrumanlar.append(gitar)
    muzisyen.caldigi_enstrumanlar.append(keman)

    print(f'Ad               : {muzisyen.first_name}\n'
          f'Soyad            : {muzisyen.last_name}\n'
          f'Çaldığı Entrüman : {muzisyen.caldigi_enstrumanlar[0].brand}\n'
          f'Çaldığı Entrüman : {muzisyen.caldigi_enstrumanlar[0].model}\n'
          f'Çıkardığı Ses    : {gitar_service.call_sound()}\n'
          f'Akor Durumu      : {gitar_service.harmonize()}')


main()

# endregion