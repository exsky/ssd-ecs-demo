import csv
import json
from time import sleep
from matplotlib import image as mpimg
from matplotlib import pyplot as plt
from subprocess import call
from libs.imggen import gen
from libs.fakegen import justify
from libs.horoscope import get_12_horo, download_fortune


def main():
    call(["echo", "monster cado~ open!!"])
    # call(["mpg123", "-a", "hw:0,3", "soundtracks/08-duel-start.mp3"])
    # TODO: update fort every morning
    print('快速取得本日運勢資料 ...')
    download_completed = download_fortune()
    if download_completed:
        print('快速取得本日運勢資料 ... 完成')

    detected_guy = None
    while True:
        detected_guy = justify()  # 看臉判斷出人名
        if not detected_guy:
            print('沒人 ...')
            sleep(1)
            continue

        # match someone
        print('抓到了！！ 是 {} !'.format(detected_guy))
        if detected_guy:
            gen(detected_guy)
            # show the img to monitor
            img = mpimg.imread('tmp/{}.png'.format(detected_guy))
            plt.ion()
            imgplot = plt.imshow(img)
            imgplot.axes.get_xaxis().set_visible(False)
            imgplot.axes.get_yaxis().set_visible(False)
            plt.show()
            plt.pause(5)  # show 5 secs
            plt.close()
            continue

if __name__ == '__main__':
    main()
