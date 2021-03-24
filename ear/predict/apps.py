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

class PredictConfig(AppConfig):
    name = 'predict'
    directory = "media/" # Image Save path
    config = InferenceConfig()
    config.display()
    model = modellib.MaskRCNN(mode="inference", config=config, model_dir="/logs")
    model.load_weights("static/Weight/mask_rcnn_eardrum_0043.h5", by_name=True)
    classificationModel = build_model(6)
    classificationModel.load_weights("static/Weight/efficientNetB0.h5")
    @staticmethod
    def detect_roi(self, image_path=None):
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
                            title="Predictions",filename="media/"+"detected"+image_path)
        # Save Croped Image
        skimage.io.imsave(self.directory+"cropped"+image_path, crop_image)

        return r['rois'].shape[0]
    @staticmethod
    def predictEardiease(self,image_path):
        # Preprocess : Resize and CLAHE
        img=preprocess(self.directory+"cropped"+image_path)

        # Predict
        prediction = self.classificationModel.predict(img, verbose=1)

        # Find Max value's Index
        max_value=max(prediction[0])
        print(max_value)
        idx = np.where(prediction[0]==max_value)[0][0]

        return idx, max_value
    @staticmethod
    def predict(self, image_path):
        result=self.detect_roi(self, image_path=image_path)
        idx = 6
        max_value = 0
        if result > 0:
            idx, max_value = self.predictEardiease(image_path)
        packet = str(result) + " " + str(idx) + " " + str(max_value)
        print(packet)