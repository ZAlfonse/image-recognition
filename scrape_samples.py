import os
import requests
from bs4 import BeautifulSoup

term = 'gull'
prefix = 'samples/' + term + '/positive_images'
desired_images = 100
page_size = 20
start_index = 200

os.makedirs('samples/' + term + '/positive_images', exist_ok=True)

for page in range(int(desired_images / page_size)):
    image_index = start_index + (page_size * page)

    url = 'https://www.google.com/search?q={term}&tbm=isch&start={index}'.format(term=term, index=image_index)
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')

    imgs = soup.findAll("img")
    for i, img in enumerate(imgs):
        img_url = img.attrs['src']
        r = requests.get(img_url, stream=True)
        with open(prefix + '/{term}'.format(term=term) + str(i + image_index) + '.jpg', 'wb+') as f:
            print(f)
            for chunk in r:
                f.write(chunk)
