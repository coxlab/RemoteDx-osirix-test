#
# Simple microservice that accepts connections on localhost,
# accepts messages for the image header and image data, and then
# run some function on it and send back a result.

import time
import zmq
import mammogram_header_pb2 as mammo
import mammogram_result_pb2 as mammo_result

import numpy as np
import matplotlib.pylab as plt
from matplotlib import cm

# only needed for the test files during the development
import pickle as pkl

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

im = None

plt.imshow(np.zeros((100, 100)))

#  Wait for next request from client
while True:

    print("Waiting for connection.... ")
    # receive a header message
    message = socket.recv()
    # TW: there is no way of telling what the integrity of the message is yet...
    
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

    #
    # diagnose 
    # Bills code goes here
    # outcome = diagnose(im)
    # for now just pickle load some sample outcome
    f = open('C:/Users/twitzel/Downloads/plugin_examples2/plugin_examples2/heatmaps_DDSM/patient-491_LMLO.pkl','rb')
    heatmap = pkl.load(f,fix_imports=True,encoding='bytes')
    heatmap = heatmap.astype(np.float32, copy=False)
    f.close()
    
    # Send reply back to client
    # So far the data structure is simple, with the heatmap size and tyoe (should be float for now)
    # and the cancer score. 
    result_header = mammo_result.MammogramResult()
    result_header.width = heatmap.shape[1];
    result_header.height = heatmap.shape[0];
    result_header.score = 0.5;
    result_header.imtype = 2; # FLOAT32

    message = result_header.SerializeToString()
    socket.send(message)

    # Send the "heatmap" result overlay
    socket.send(heatmap.tostring(order='C'))
    
    # show it, tnis is probably not needed in production mode, but useful for debugging
    plt.imshow(im, cmap='gray')
    plt.show()


