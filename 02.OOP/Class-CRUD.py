from uuid import uuid4
from pprint import pprint
categories ={}

class Category :
    def __init__(self, name:str,description:str):
        self.description=description
        self.name=name
        self.id=uuid4()

class Category_Service:
    def create(self,category_obj:Category)->None:
        categories[str(category_obj.id)]={
            'name':category_obj.name,
            'description':category_obj.description
        }

        print(f'{category_obj.name} has been created')
    def get_all(self,db:dict)->None:
        pprint(db)
    def get_by_id(self,id:str)->dict:
        for i in categories.keys():
            if i == id:
                return categories.get(id)

    def update(self,id:str,name:str,description:str):
        current_category=self.get_by_id(id)
        current_category.update({
            'name':name,
            'description':description
        })

    def delete(self,id:str)->None:
        current_category=self.get_by_id(id)

        if current_category!={}:
            del categories[id]
            print('Category has been deleted..!')
        else:
            print('There is no such category..!')

def main():
    while True :
        service = Category_Service()
        process=input('Please type a transaction name : ').lower()

        match process:
            case 'exit':
                print('Applecation has benn closing..!')
                break
            case 'create':
                category_name=input('Category Name : ')
                category_description=input('Description : ')
                category_obj=Category(name=category_name,description=category_description)
                service.create(category_obj)
                service.get_all(categories)
            case 'get all':
                service.get_all(categories)
            case 'get by id':
                id = input('Id: ')
                pprint(service.get_by_id(id))
            case 'update':
                id=input('id : ')
                category_name = input('Category Name : ')
                category_description = input('Description : ')
                service.update(id=id,name=category_name,description=category_description)
                pprint(service.get_by_id(id))
            case 'delete':
                id=input('id :')
                service.delete(id)
            case _:
                print('Please type a correfct transaction name..!')

main()