import requests
from bs4 import BeautifulSoup
import pprint as p

url = 'https://holamundo.day'
r = requests.get(url)

if r.status_code == 200:
    print("conexion", r.status_code)
else:
    print(r.status_code)

soup = BeautifulSoup(r.text, "html.parser")
p.pprint(soup)
print("============================================")
content = soup.find_all("blockquote")
for data in content[21:]:
    print(data.text)

# print(content)
