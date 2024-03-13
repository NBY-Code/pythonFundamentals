#Product adında bir Dictionary oluşurup id isim kategori vb . özelliklerini doldurup küçük bir CRUD operasyonu deneyelim.
from uuid import uuid4 # burada idnin uniqe olaması sağlanmaktadır
from pprint import pprint # pprint yazım formatı dicitonary olarak yazmayı sağlar
def create_product(product):
    product_id = str(uuid4())
    product_name = input('Product Name : ')
    category_name = input('Category Name : ')
    stock = int(input('Stock : '))
    price = input('Price : ')
    product[product_id] = {
        'product_name': product_name,
        'category_name': category_name,
        'stock': stock,
        'price': price
    }
def update_product(product):
    product_id = input('Type id : ')
    product_name = input('Product Name : ')
    category_name = input('Category Name : ')
    stock = int(input('Stock : '))
    price = input('Price : ')
    product.update({
        product_id: {
            'product_name': product_name,
            'category_name': category_name,
            'stock': stock,
            'price': price
        }
    })
    print(f"{product_id} has been edited ..! ")
def list_product(product):
    pprint(product)
def delet_product(product):
    product_id = input('Type id : ')
    del product[product_id]
    print(f"{product_id} has been deleted ..! ")
def manuel_guide():
    product={}
    while True:
        print('Manuel Guide\n'
            '==============\n'
            'Create\n'
            'List\n'
            'Update\n'
            'Delete\n'
            'Exit')
        process=input('Type your process upon mauel guide : ').lower()
        if process == 'create':
            create_product(product)
        elif process == 'list':
            list_product(product)
        elif process == 'update':
            update_product(product)
        elif process == 'delete':
            delet_product(product)
        elif process == 'exit':
            print('Application has been closing..!')
            break
        else:
            print('Please type valid process name..!')
manuel_guide()