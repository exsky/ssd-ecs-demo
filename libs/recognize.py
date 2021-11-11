import os
import cv2
import json
import boto3
import numpy as np
import mxnet as mx
from matplotlib import pyplot as plt
from collections import namedtuple


class CHTVisu:

    def __init__(self):
        SHAPE = 512
        input_shapes=[('data', (1, 3, SHAPE, SHAPE))]
        confidence_threshold = 0.2
        CLASSES = ['changty','sky','roger','jimmy','kfira','rachael','rinns','tclan']

    def get_ctx(self):
        try:
            gpus = mx.test_utils.list_gpus()
            if len(gpus) > 0:
                ctx = []
                for gpu in gpus:
                    ctx.append(mx.gpu(gpu))
            else:
                ctx = [mx.cpu()]
        except:
            ctx = [mx.cpu()]
        return ctx

    def justify(self, j_image):
        ctx = self.get_ctx()
        # Load Module
        param_path = os.path.join(TMP_FOLDER, 'ssd_vgg16_512')
        # print("param_path: {}".format(param_path))
        sym, arg_params, aux_params = mx.model.load_checkpoint(param_path, 0)
        mod = mx.mod.Module(symbol=sym, label_names=[], context=ctx)
        mod.bind(for_training=False, data_shapes=input_shapes)
        mod.set_params(arg_params, aux_params)
        Batch = namedtuple('Batch', ['data'])
        if not j_image:
            j_image = 'images/line_637669196787939.jpg'
        results, org_image = infer(j_image)
        detected_guy = CLASSES[int(results[0][0]))
        return detected_guy

    def predict_from_file(self, filepath, reshape=(SHAPE, SHAPE)):
        # Switch RGB to BGR format (which ImageNet networks take)
        img = cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2RGB)
        if img is None:
            return []
         # Resize image to fit network input
        img = cv2.resize(img, reshape)
        org_image = img.copy()
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 1, 2)
        img = img[np.newaxis, :]
        mod.forward(Batch([mx.nd.array(img)]))
        prob = mod.get_outputs()[0].asnumpy()
        prob = np.squeeze(prob)
        return prob, org_image

    def infer(self, image_path, threshold=confidence_threshold):
        results, org_image = self.predict_from_file(image_path)
        image_name = image_path.split("/")[-1]
        filtered_result = results[results[:, 0] != -1]
        filtered_result = filtered_result[filtered_result[:, 1] >=threshold]
        return filtered_result, org_image
