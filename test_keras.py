import numpy as np
from keras.preprocessing import image
from keras.applications import vgg16

# Load Keras' VGG16 model that was pre-trained against the ImageNet database
model = vgg16.VGG16()

print("test_keras ok!")
