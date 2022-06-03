import requests
import threading
import os
import json

try:
    os.mkdir("web_images")
except FileExistsError:
    pass

with open("task_urls.json") as file:
    urls = json.load(file)
path = "web_images"


def downloading(url, name):
    global response
    if response.status_code == 200:
        with open("web_images/" + "image" + name + ".png", "wb") as images:
            images.write(response.content)


runs = []
for i, url in enumerate(urls["items"]):
    x = threading.Thread(target=downloading, args=(url["url"], str(i)))
    try:
        response = requests.get(url['url'])
    except requests.exceptions.ConnectionError:
        print("Connection issues try again")
        break
    x.start()
    runs.append(x)

for x in runs:
    x.join()
if os.path.exists(path) and len(os.listdir(path)) == 0:
    print(f"Directory 'web images' was deleted ")
    os.rmdir(path)
else:
    print(f"Downloaded {len(os.listdir(path))} images")
