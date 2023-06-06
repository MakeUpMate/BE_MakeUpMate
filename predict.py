import numpy as np
import tensorflow as tf
from keras.utils import img_to_array, load_img

class predict:
    def __init__(self,filename):
        self.filename =filename


    def skinClassifier(self):
        model_path = "workspaceML\model.h5"
        loaded_model = tf.keras.models.load_model(model_path)

        img=load_img("static\img\inputImage.jpg", target_size=(150, 150))
        x=img_to_array(img)
        x /= 255
        x=np.expand_dims(x, axis=0)
        images = np.vstack([x])
        pred = loaded_model.predict(images, batch_size=10)
        
        class_result = 0
        temp = 0
        counter = 0

        for i in pred[0]:
            counter+=1
            if i > temp:
                temp = i
                class_result = counter

        return class_result