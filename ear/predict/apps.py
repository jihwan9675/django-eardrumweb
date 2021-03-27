from django.apps import AppConfig
import os, sys, json, datetime, cv2, skimage.draw
import numpy as np
from mrcnn.visualize import display_instances
import matplotlib.pyplot as plt
from mrcnn import utils
from mrcnn import visualize
from mrcnn.visualize import display_images
import mrcnn.model as modellib
from mrcnn.model import log
from mrcnn import model as modellib, utils
from modules.CustomConfig import CustomConfig, InferenceConfig
from modules.preprocess import preprocess
from modules.build_model import build_model
import tensorflow as tf
from tensorflow.python.keras.backend import set_session


class predictmodel():
    eardrum = ["Normal","Traumatic Perforation", "Acute Otitis Media", "Chronic Otitis Media",
            "Congential Cholesteatoma", "Otitis Media with Effusion", "I don't know"]
    sess = tf.compat.v1.Session()
    graph = tf.compat.v1.get_default_graph()
    set_session(sess)
    directory = "media/" # Image Save path
    config = InferenceConfig()
    config.display()
    model = modellib.MaskRCNN(mode="inference", config=config, model_dir="/logs")
    model.load_weights("static/Weight/mask_rcnn_eardrum_0043.h5", by_name=True)
    classificationModel = build_model(6)
    classificationModel.load_weights("static/Weight/efficientNetB0.h5")
   

    def detect_roi(self, image_path):
        with self.graph.as_default():
            set_session(self.sess)
            print("media/"+image_path)
            image = skimage.io.imread("media/"+image_path)

            # Detect/Predict
            r = self.model.detect([image], verbose=1)[0]

            # No instance == dont need classification
            if r['rois'].shape[0] == 0: 
                return r['rois'].shape[0]

            # Detected Object's Range --> For Cropping
            y1, x1, y2, x2 = r['rois'][0] 
            crop_image=image[y1:y2,x1:x2]

            # Save Image include Detected information
            visualize.display_instances(image, r['rois'], r['masks'], r['class_ids'], 
                                "Ear", r['scores'], 
                                title="Predictions",filename="media/"+"d_"+image_path)
            # Save Croped Image
            skimage.io.imsave(self.directory+"c_"+image_path, crop_image)

            return r['rois'].shape[0]


    def predictEardiease(self,image_path):
        with self.graph.as_default():
            set_session(self.sess)
            # Preprocess : Resize and CLAHE
            img=preprocess(self.directory+"c_"+image_path)

            # Predict
            prediction = self.classificationModel.predict(img, verbose=1)

            # Find Max value's Index
            Accuracy=max(prediction[0])
            idx = np.where(prediction[0]==Accuracy)[0][0]

            return idx, Accuracy

    def predict(self, image_path):
        detected_instance_count=self.detect_roi(image_path=image_path)
        idx = 6
        Accuracy = 0
        if detected_instance_count > 0:
            idx, Accuracy = self.predictEardiease(image_path)
        
        # return list ...  [DiseaseName, Count of Detected Instance, Accuracy]
        return [self.eardrum[idx], detected_instance_count, Accuracy]

class PredictConfig(AppConfig):
    name = 'predict'
    just = predictmodel()