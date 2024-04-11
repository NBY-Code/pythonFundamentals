#Kalıtım
#Ata bir sınfıtaki bilgilerin o sınıfı kalıtım alan child classın bu ata sınfıın özelliklerini alamasına deriz. Amaç kod tekrarına düşmeden ortak olarak alınan  özellikleri tek bir yerde toplayrak yazılım prensiplerine uymaktır.


from uuid import uuid4
from datetime import datetime
from socket import gethostname,gethostbyname
from enum import Enum

employees = []

class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3

class BaseEntity:
    def __init__(self, first_name:str,last_name:str,departmant:str):
        self.departman = departmant
        self.last_name=last_name
        self.first_name=first_name
        self.id=str(uuid4())
        self.status=Status.Active.name
        self.create_date=datetime.now()
        self.create_ip_adress=gethostbyname(gethostname())
        self.create_machine_name=gethostname()
class Employee(BaseEntity):
    pass
class Emplyoee_Service:
    def create(self,employee:Employee):
        employees.append(employee)
        print(f'{employee.first_name}{employee.last_name} has been created..!')
    def get_all(self):
        for item in employees:
            print(f'{item.__dict__}')

    def get_by_full_name(self, full_name:str):
        for employee in employees:
            if f'{employee.first_name} {employee.last_name}'.lower().__contains__(full_name):
                print(employee.__dict__)

    def get_not_passive(self):
        for employee in employees:
            if employee.status=='Active'or employee.status=='Modifed':
                print(employee.__dict__)

def main():
    service=Emplyoee_Service()

    while True:
        process = input('Type Process : ')

        match process:
            case 'create':
                first_name=input('First Name : ')
                last_name=input('last Name : ')
                departmant=input('Departmant : ')
                employee=Employee(first_name=first_name,last_name=last_name,departmant=departmant)
                service.create(employee)
            case 'get all':
                service.get_all()
            case 'get by name':
                full_name=input('Full Name: ')
                service.get_by_full_name(full_name)
main()