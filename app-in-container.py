import os
import csv
import sys
import json
import asyncio
import argparse
from time import sleep
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
from matplotlib import use as mpuse
from subprocess import call
from libs.imggen import gen
#from libs.fakegen import justify
from libs.capture import cap_from_cam, capture_from_cam
from libs.horoscope import get_12_horo, download_fortune
from libs.recognize import CHTVisu

from detect.detector import Detector
from symbol.symbol_factory import get_symbol
from dataset.cv2Iterator import CameraIterator
import logging

def parse_args():
    parser = argparse.ArgumentParser(description='Single-shot detection network demo')
    parser.add_argument('--network', dest='network', type=str, default='vgg16_reduced',
                        help='which network to use')
    parser.add_argument('--prefix', dest='prefix', help='trained model prefix',
                        default=os.path.join(os.getcwd(), 'trained-model', 'ssd_'),
                        type=str)
    parser.add_argument('--cpu', dest='cpu', help='(override GPU) use CPU to detect',
                        action='store_true', default=False)
    parser.add_argument('--gpu', dest='gpu_id', type=int, default=0,
                        help='GPU device id to detect with')
    parser.add_argument('--data-shape', dest='data_shape', type=str, default='512',
                        help='set image shape')
    parser.add_argument('--mean-r', dest='mean_r', type=float, default=123,
                        help='red mean value')
    parser.add_argument('--mean-g', dest='mean_g', type=float, default=117,
                        help='green mean value')
    parser.add_argument('--mean-b', dest='mean_b', type=float, default=104,
                        help='blue mean value')
    parser.add_argument('--thresh', dest='thresh', type=float, default=0.5,
                        help='object visualize score threshold, default 0.6')
    parser.add_argument('--nms', dest='nms_thresh', type=float, default=0.5,
                        help='non-maximum suppression threshold, default 0.5')
    parser.add_argument('--no-force', dest='force_nms', action='store_false',
                        help='dont force non-maximum suppression on different class')
    parser.add_argument('--no-timer', dest='show_timer', action='store_false',
                        help='dont show detection time')
    parser.add_argument('--deploy', dest='deploy_net', action='store_true', default=False,
                        help='Load network from json file, rather than from symbol')
    parser.add_argument('--class-names', dest='class_names', type=str,
                        default='aeroplane, bicycle, bird, boat, bottle, bus, \
                        car, cat, chair, cow, diningtable, dog, horse, motorbike, \
                        person, pottedplant, sheep, sofa, train, tvmonitor',
                        help='string of comma separated names, or text filename')
    parser.add_argument('--camera', action='store_true',
                        help="use camera for image capturing")
    parser.add_argument('--frame-resize', type=str, default=None,
                        help="resize camera frame to x,y pixels or a float scaling factor")
    args = parser.parse_args()
    return args

async def recogn():
    # Set vars
    detected_guy = None
    chtv = CHTVisu()
    while True:
        await asyncio.sleep(0.1)
        detected_guy = chtv.justify('live.jpg')  # 看臉判斷出人名
        #detected_guy = justify()  # 看臉判斷出人名
        if not detected_guy:
            print('沒人 ...')
            await asyncio.sleep(0.2)
            continue
        # match someone
        print('抓到了！！ 是 {} !'.format(detected_guy))
        if detected_guy:
            # play
            # call(["mpg123", "statics/john_cena.mp3"])
            # generate daily fortune talk
            gen(detected_guy)
            # show the img to monitor
            img = mpimg.imread('tmp/{}.png'.format(detected_guy))
            mpuse('TkAgg')
            plt.ion()
            imgplot = plt.imshow(img)
            imgplot.axes.get_xaxis().set_visible(False)
            imgplot.axes.get_yaxis().set_visible(False)
            plt.show()
            await asyncio.sleep(2)
            plt.pause(5)  # show 5 secs
            plt.close()
            continue
    return

def main():
    # Enable logging
    logging.getLogger().setLevel(logging.INFO)
    logging.basicConfig(format='%(asctime)-15s %(message)s')
    # Prepare for the daily talks
    # call(["mpg123", "-a", "hw:0,3", "soundtracks/08-duel-start.mp3"])
    # TODO: update fort every morning
    # Download fortune talk
    download_fortune()
    # Setup of coroutine
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    tasks = [ capture_from_cam(0), recogn() ]
    # tasks = [ recogn() ]
    # tasks = [ capture_from_cam(0) ]
    group = asyncio.gather(*tasks)
    loop.run_until_complete(group)
    loop.close()
    return

if __name__ == '__main__':
    sys.exit(main())
