# Encapsulation (Veri Gizleme)
#Bir sınıfta bulunan bir propertye olan erişimi engelleyerek başka sınfılar tarafında görülmesine veya değiştirilmesine izin vermemek amaçıyla kullanılır erişilmediği için değiştirilmeside başka sınıflar tarafından mümkün olmaz.
from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint


class Status(Enum):
    Active = 1,
    Modified = 2,
    Passive = 3


class BaseEntity:
    def __init__(self):
        self.__id = ''
        self.__created_date = ''
        self.__created_computer_name = ''
        self.__created_ip_address = ''
        self.__status = ''

    # Not : double underscore ile tanımladığımız alanlara ne sınıfın örnekleminden (instance) nede bu sınıfın kalıtım alan alt sınıfından örnekleminden erişebiliyorum.Encaposule ettiğim alanlara sadece sınfıın yaşam alanında erişebiliyorum.Aşağıda da bir custom function yazarak bu private alanlara değer atadık.
    def set_values_private_attribute(self):
        self.__id = uuid4()
        self.__created_date = datetime.now()
        self.__created_computer_name = gethostname()
        self.__created_ip_address = gethostbyname(gethostname())
        self.__status = Status.Active.name

    def show_information(self):
        return self.__dict__
class Car(BaseEntity):
    def __init__(self, brand: str, model: str):
        super().__init__()
        self.model = model
        self.brand = brand
        self.__price=0
        self.__sase_no=0
    def set_values_private_attribute(self,price):
        if  price>0:
            super().set_values_private_attribute()
            self.__sase_no=uuid4()
            self.__price=price
            print('Car has been created..!')
            pprint(self.__dict__)
c1 = Car('Dodge','Viper')
c1.set_values_private_attribute(42500)