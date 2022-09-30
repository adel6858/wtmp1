import requests 
from bs4 import BeautifulSoup as bs
import json

url = 'https://calorizator.ru/product'

r = requests.get(url)
repl = r.text
#print(r.text)

with open('index.html', "w", encoding="utf-8") as f:
    f.write(repl)

with open('index.html', encoding="utf-8") as f:
    src= f.read()

soup = bs(src,"lxml")
all_prd_links =  soup.find_all("ul" ,class_="product")


for_all_prod_dict = {}
for item in all_prd_links:
    soup=bs(f"{item}",'html.parser')
    item_name = soup.a.text
    item_href = "https://calorizator.ru/" + soup.a.attrs["href"]
    
    for_all_prod_dict [item_name] = item_href

with open('for_all_prod_dict.json', 'w', encoding="utf-8") as file:
    json.dump(for_all_prod_dict, file, indent=4, ensure_ascii=False)

with open('for_all_prod_dict.json',encoding="utf-8") as file:
    for_all_prod = json.load(file)



for item_name, item_href in for_all_prod:
    req_1 = requests.get(url = item_href)
    src_1 = req_1.text
    print(src_1)

# prodolzhit'
    



    


  