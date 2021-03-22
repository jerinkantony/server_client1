import requests 
import time
from PIL import Image


url = 'http://192.168.38.8:5000/im_size' #ML2
#url = 'http://127.0.0.1:5000/im_size'   #Localhost

my_img = {'image': open('0.jpg', 'rb')}

payload = {'id': '123', 'type': 'jpg'}

start = time.time()
r = requests.post(url, files=my_img, data=payload)

print('time for round trip:',time.time()-start)
# convert server response into JSON format.
print(r.json())

'''
start = time.time()
img = Image.open("/home/skycam/basics/opencv_basics/encode_decode/0.jpg")
print(img.width, img.height)
print('Time:',time.time()-start)
'''

