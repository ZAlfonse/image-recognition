import os
import requests
from bs4 import BeautifulSoup
import base64




term = 'gull'
prefix = 'samples/'+term+'/positive_images'

os.makedirs('samples/'+term+'/positive_images', exist_ok=True)

url = 'https://www.google.com/search?q={term}&tbm=isch'.format(term=term)
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
with open('out.html', 'w+') as f:
    f.write(html)
birbs = soup.findAll("img", {"class" : "rg_ic" })
print(birbs)
for birb in birbs:
    print(birb.src)

def decode_image_data_to_file(bytes, filename):
    with open('samples/'+term+'/positive_images'+filename, 'wb') as f:
        f.write(base64.decodebytes(string))
