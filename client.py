import requests 
import time
from PIL import Image
import multiprocessing
import os


def worker_client(i):
    
    print ('Worker',i)
    
    url = 'http://127.0.0.1:5000/im_size'   #Localhost
    #url = 'http://192.168.38.8:5000/im_size' #ML2
    
    imgnam = os.path.join('client_images', str(i)+'.jpg')
    my_img = {'image': open(imgnam, 'rb')}

    payload = {'id': '123', 'type': 'jpg'}

    start = time.time()
    r = requests.post(url, files=my_img, data=payload)

    print('time for round trip of {}:'.format(i),time.time()-start)
    # convert server response into JSON format.
    #print(r.json())


def worker(i):
    """worker function"""
    print ('Worker',i)
    time.sleep(1)
    
    return

if __name__ == '__main__':
    start2=time.time()
    jobs = []
    parcalls=5
    for i in range(parcalls):
        p = multiprocessing.Process(target=worker_client, args=(i,))
        jobs.append(p)
        p.start()
    for j in jobs:
        j.join()
    print('******* Time per call:',(time.time()-start2)/parcalls)

'''
start = time.time()
img = Image.open("/home/skycam/basics/opencv_basics/encode_decode/0.jpg")
print(img.width, img.height)
print('Time:',time.time()-start)
'''

