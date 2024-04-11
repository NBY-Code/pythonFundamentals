
from abc import abstractmethod,ABC
from datetime import datetime

#NOT : Artık nesnelerimzi temsil eden sınıfların içersiine CRUD operasyonlarını temsil eden fonksiyonları yazmıyoruz.Nesne farklı bir sınıf CRUD operasyonlarını içeren fonksiyonlar ise farklı bir sınıf olacak.Bu bağlamda lab_04 'teki fatura ödeme uygulamasını soyutlama ile ve yukarıedaki mantığa göre yapalım.

class BaseBill:
    def __init__(self , bill_name : str,value_add_task:float,amount:float):
        self.bill_name = bill_name
        self.value_add_task = value_add_task
        self.amount = amount
class ElectrictyBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float,kw:float):
        super().__init__(bill_name, value_add_task, amount)
        self.kw=kw
class WaterBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float,mill:float):
        super().__init__(bill_name, value_add_task, amount)
        self.mill=mill
class NaturalGasBill(BaseBill):
    def __init__(self, bill_name: str, value_add_task: float, amount: float,m3:float):
        super().__init__(bill_name, value_add_task, amount)
        self.m3=m3

class BaseService(ABC):
    @abstractmethod
    def calculate_bill(self ,bill:BaseBill)->float:pass

    def create_log(self,bill:BaseBill,result:float):
        with open(file='OOP_Princple_bill_info.txt' , mode='a',encoding='utf_8')as file:
            file.write(f'Bill Name = {bill.bill_name}\n'
                       f'Total Amount = {result}\n'
                       f'Create Date = {datetime.now()}')

class WaterBillService(BaseService):
    def calculate_bill(self, bill: WaterBill) -> float:
        return bill.amount*bill.value_add_task*bill.mill

class ElectrictyBillService(BaseService):
    def calculate_bill(self, bill: ElectrictyBill) -> float:
        return bill.amount*bill.value_add_task*bill.kw

class NaturalGasBillService(BaseService):
    def calculate_bill(self, bill: NaturalGasBill) -> float:
        return bill.amount*bill.value_add_task*bill.m3


water_bill=WaterBill('ISKI',12.3,34.5,56.7)
water_service=WaterBillService()
result=water_service.calculate_bill(water_bill)
water_service.create_log(water_bill,result)