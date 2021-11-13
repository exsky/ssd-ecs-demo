import csv
import json
from time import sleep
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
            continue

if __name__ == '__main__':
    main()
