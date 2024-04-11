from pprint import pprint
from requests import get

# response = get('https://newsapi.org/v2/everything?q=tesla&from=2024-02-13&sortBy=publishedAt&apiKey=46cc50cf165344ad9994c9a488767c39')
#
# data = response.json()
# pprint(data)
# pprint(f'Author :{data["articles"][0]["author"]}')
# pprint(f'Title :{data["articles"][0]["title"]}')
# pprint(f'Pulished Date :{data["articles"][0]["publishedAt"]}')
# pprint((f'Description: {data["articles"][0]["description"]}'))
#
# #Kullanıcıdan yazar ismi alınıcak ve bu yazarın maklesi ekrana basılıcak
# author_Name = input("Author Name : ")
# for article in data["articles"]:
#     if author_Name == article.get("author"):
#         pprint(article)
url="https://restcountries.com"
response=get(url)
data=response.json()
pprint(data)