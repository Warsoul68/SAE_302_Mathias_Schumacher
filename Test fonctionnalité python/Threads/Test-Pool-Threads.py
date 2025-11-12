import time
import concurrent.futures
import requests

img_urls = [
    'https://tse4.mm.bing.net/th/id/OIP.8dw34HUZyV52Wvq7SnjlqQHaHa?rs=1&pid=ImgDetMain&o=7&rm=3',
    'https://th.bing.com/th/id/R.4f585f42fe38806f2efef4e09d67281d?rik=3f6AV635GyXiNA&pid=ImgRaw&r=0',
    'https://www.freeiconspng.com/uploads/apple-computer-laptop-mac-monitor-screen-icon--icon-search--16.png',
]

def download_image(img_url):
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[4]
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f"{img_name} was downloaded")

if __name__ == '__main__':
    start = time.perf_counter()

    with concurrent.futures.ThreadPoolExecutor() as executor: #for img_url in img_urls:
        executor.map(download_image, img_urls)
    
    end = time.perf_counter()
    print(f"Tasks ended in {round(end - start, 2)} second(s)")