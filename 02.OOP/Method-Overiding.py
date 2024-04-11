#Metod overiding
#Ata sınfıta bulunan metodları bu ata sınıfları kalıtım alan başka sınıflarda ezerek yeni işlevler kazandırılmasına denilir.

from datetime import datetime

class BaseBill:
    def __init__(self, bill_name: str, values_add_task: float, amount: float):
        self.bill_name = bill_name
        self.values_add_task = values_add_task
        self.amount = amount

    def calculate_bill(self):
        return self.amount * self.values_add_task

    def create_log(self):
        with open(file='bill_info.txt',mode='a',encoding='utf-8')as file :
            file.write(f'Bill Name : {self.bill_name}\n'
                       f'Total Amount :{self.calculate_bill()}\n'
                       f'Create Date : {datetime.now()}')
class Water_Bill(BaseBill):
    def __init__(self, bill_name: str, values_add_task: float, amount: float, mil: float):
        super().__init__(bill_name, values_add_task, amount)
        self.mill = mil

    def calculate_bill(self):
        return super().calculate_bill() * self.mill

class Electricity_Bill(BaseBill):
    def __init__(self, bill_name: str, values_add_task: float, amount: float, kw: float):
        super().__init__(bill_name, values_add_task, amount)
        self.kw = kw

    def calculate_bill(self):
        return super().calculate_bill() * self.kw

class Naturel_Gas_Bill(BaseBill):
    def __init__(self, bill_name: str, values_add_task: float, amount: float, m3: float):
        super().__init__(bill_name, values_add_task, amount)
        self.m3 = m3

    def calculate_bill(self):
        return super().calculate_bill() * self.m3

w1 = Water_Bill(bill_name='water bill', values_add_task=18, amount=1, mil=10)
w1.create_log()

e1 = Electricity_Bill(bill_name='Electricity bill', values_add_task=18, amount=1, kw=15)
e1.create_log()

NG1 = Naturel_Gas_Bill(bill_name='Naturel Gas bill', values_add_task=18, amount=1, m3=20)
NG1.create_log()