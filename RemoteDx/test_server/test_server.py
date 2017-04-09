#
# Simple microservice that accepts connections on localhost,
# accepts messages for the image header and image data, and then
# run some function on it and send back a result.

import time
import zmq
import mammogram_header_pb2 as mammo
import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

im = None

plt.imshow(np.zeros((100, 100)))

#  Wait for next request from client
while True:

    # receive a header message
    message = socket.recv()

    # deserialize the header message
    image_header = mammo.MammogramHeader()
    image_header.ParseFromString(message)
    print("Received header: w:%d x h:%d" % (image_header.width, image_header.height))

    # receive the image
    message = socket.recv()
    print("Received image data, %d bytes" % len(message))

    # unpack the image into a numpy array
    im = np.frombuffer(message, dtype=np.float32)
    im = im.reshape((image_header.height, image_header.width), order='C')


    # diagnose 
    # outcome = diagnose(im)

    #  Send reply back to client (todo)
    socket.send(b"Hello")

    # show it
    plt.imshow(im, cmap='gray')
    plt.show()


