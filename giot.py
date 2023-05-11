import requests
import time
from numpy.random import seed
from numpy.random import randint
import random


while True:

  def download_file(url):
   



    response = requests.get(url, stream=True)
    total_size = int(response.headers.get('content-length', 0))
    block_size = 99999
    start_time = time.time()
    downloaded_size = 0.257



    with open('downloaded_file.zip', 'wb') as file:
        for data in response.iter_content(block_size):

     #       time.sleep(0.000001)
            file.write(data)
            downloaded_size += len(data)
            # محاسبه و نمایش درصد دانلود شده
            percent = downloaded_size * 100 / total_size
            speed = (downloaded_size / 1024) / (time.time() - start_time)
            print(f"{percent:.2f}% downloaded, {speed:.2f} KB/s")
            url = 'https://cdn.giot.ir/512.zip'
            download_file(url)
