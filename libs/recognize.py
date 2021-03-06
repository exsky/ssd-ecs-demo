import os
import json
import boto3
import numpy as np
import mxnet as mx
from collections import namedtuple
import cv2


class CHTVisu:
    pic_size = 0
    #width, height = image.size
    confidence_threshold = 0
    input_shapes = None
    candidates = None
    mod = None
    batch = None

    def __init__(self):
        self.pic_size = 512
        self.confidence_threshold = 0.2
        self.input_shapes = [('data', (1, 3, self.pic_size, self.pic_size))]
        self.candidates = [
             'sky', 'tclan', 'william', 'yiming',
             'rachael', 'michael', 'hugo', 'yugioh',
             'changty', 'rinns', 'jimmy', 'kfira' ]
        self.preload()

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

    def preload(self):
        ctx = self.get_ctx()
        # Load Module
        param_path = os.path.join('trained-model/', 'ssd_vgg16_512')
        # print("param_path: {}".format(param_path))
        sym, arg_params, aux_params = mx.model.load_checkpoint(param_path, 0)
        self.mod = mx.mod.Module(symbol=sym, label_names=[], context=ctx)
        self.mod.bind(for_training=False, data_shapes=self.input_shapes)
        self.mod.set_params(arg_params, aux_params)
        self.batch = namedtuple('Batch', ['data'])

    def justify(self, j_image=None):
        print('Load image ...')
        if not j_image:
            j_image = 'images/changty.jpg'
            # j_image = 'images/line_637688508478694.jpg' # jimmy
        results, org_image = self.infer(j_image)
        specificed_man = None
        if len(results) > 0:
            try:
                specificed_man = int(results[0][0])
            except Exception as e:
                print(e)
        if specificed_man:
            detected_guy = self.candidates[specificed_man]
            #print(detected_guy)
            return detected_guy
        else:
            #print('not found')
            return None

    def predict_from_file(self, filepath):
        # Switch RGB to BGR format (which ImageNet networks take)
        img = cv2.cvtColor(cv2.imread(filepath), cv2.COLOR_BGR2RGB)
        if img is None:
            return []
        # Resize image to fit network input
        reshape = (self.pic_size, self.pic_size)
        img = cv2.resize(img, reshape)
        org_image = img.copy()
        img = np.swapaxes(img, 0, 2)
        img = np.swapaxes(img, 1, 2)
        img = img[np.newaxis, :]
        self.mod.forward(self.batch([mx.nd.array(img)]))
        prob = self.mod.get_outputs()[0].asnumpy()
        prob = np.squeeze(prob)
        return prob, org_image

    def infer(self, image_path):
        threshold = self.confidence_threshold
        results, org_image = self.predict_from_file(image_path)
        image_name = image_path.split("/")[-1]
        filtered_result = results[results[:, 0] != -1]
        filtered_result = filtered_result[filtered_result[:, 1] >= threshold]
        return filtered_result, org_image
