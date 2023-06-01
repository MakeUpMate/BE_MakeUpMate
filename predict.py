import numpy as np
from PIL import Image
import cv2
import tensorflow as tf

class predict:
    def __init__(self,filename):
        self.filename =filename


    def skinClassifier(self):

        model_path = "model.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        imagename = self.filename
        image = cv2.imread(imagename)

        image_fromarray = Image.fromarray(image, 'RGB')
        resize_image = image_fromarray.resize((150, 150))
        expand_input = np.expand_dims(resize_image,axis=0)
        input_data = np.array(expand_input)
        input_data = input_data/255
        pred = loaded_model.predict(input_data)

        # if pred[0] > 0.5 :
        #     prediction = 'This is a dog'
        #     return [{"response": prediction}]
        # else:
        #     prediction = 'This is a cat'
        #     return [{"response": prediction}]
        
        class_result = 0
        temp = 0
        counter = 0

        for i in pred[0]:
            counter+=1
            if i > temp:
                temp = i
                class_result = counter

        return class_result