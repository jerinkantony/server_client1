from flask import Flask, request, jsonify
from PIL import Image
import time
app = Flask(__name__)

@app.route("/im_size", methods=["POST"])
def process_image():
    start = time.time()
    print('request size',"{0:.2f}".format(int(request.headers.get('Content-Length'))/1024) +'KB')

    file = request.files['image']
    print('file time:',time.time()-start)
    start2=time.time()
    # Read the image via file.stream
    img = Image.open(file.stream)

    payload = request.form.to_dict()
    print('payload:',payload)
    print('Imread+payload time:',time.time()-start2)

    #my_img = {'image': open('1.jpg', 'rb')}
    my_img=''

    print('process time:',time.time()-start)
    return jsonify({'msg': 'success', 'size': [img.width, img.height], 'img1':my_img})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

    
