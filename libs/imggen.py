import os
import json
import base64
from datetime import date
from html2image import Html2Image
from libs.person import fetch_staff_info
from libs.horoscope import get_12_horo


def loadTalkFromFile():
    with open('talk.json', 'r') as f:
        talk = json.load(f)
        return talk


# 抓到某人後，產生這個人的資料圖
def gen(name):
    guy = fetch_staff_info(name)
    if not guy:
        print('The scanned person not in model ...')
        guy = {'account_id': 'liumaosing', 'full_name': '劉昴星',
                'image_path':'images/liumaosing.jpg',
                'role_title': '廣州特級廚師', 'zodiac': 'Scorpio'}

    # 讀取樣板再來取代
    with open('pages/person.html', 'r') as file:
        page = file.read()
        t = date.today()  # 0 日期
        title_des = t.strftime("%Y年%m月%d日")
        page = page.replace('<h1>今日運勢</h1>',
                '<h1>{}</h1>'.format(title_des))
        name_des = '<h4><b>{}</b></h4>'.format(guy['full_name'])  # 1 姓名
        page = page.replace('<h4><b>劉昴星</b></h4>', name_des)
        role_des = '<p>{}</p>'.format(guy['role_title'])  # 2 職稱
        page = page.replace('<p>職稱</p>', role_des)
        all_fort = loadTalkFromFile()  # 3 運勢
        guy_fort = all_fort[guy['zodiac']]
        fort_des = '<p>{}</p>'.format(guy_fort)
        page = page.replace('<p>運勢描述</p>', fort_des)
        with open(guy['image_path'], 'rb') as image_file:  # 4 照片
            encodedencoded_str = base64.b64encode(image_file.read())
        page = page.replace('base_64_img', encodedencoded_str.decode('utf-8'))
        page = page.replace('<h5>星座</h5>','<h5>{}</h5>'.format(guy['zodiac']))
    # 生成新的網頁
    with open('pages/{}.html'.format(name), 'w') as new_file:
        new_file.write(page)

    # 列印畫面變成圖片
    hti = Html2Image('chrome')
    hti.output_path = 'tmp'
    if not os.path.exists('tmp'):
        os.makedirs('tmp')
    outname = '{}.png'.format(name)
    hti.screenshot(
            html_file='pages/{}.html'.format(name),
            save_as=outname, size=(1000, 800))
    return outname
