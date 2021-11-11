import requests
from bs4 import BeautifulSoup


def getFortune(what=None):
    if not what:
        url = "https://www.daily-zodiac.com/mobile/zodiac/Aries"
    else:
        url = "https://www.daily-zodiac.com/mobile/zodiac/{}".format(what)
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        result = soup.find("article").getText()
        result = result.replace('\n', '')
        result = result.replace(' ', '')
    except Error as e:
        print(e)
    return result


def get_12_horo():
    fortunes = {}
    zodiac = [ 'Aries', 'Taurus', 'Gemini', 'Cancer',
               'Leo', 'Virgo', 'Libra', 'Scorpio',
               'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
               ]
    for z in zodiac:
        fortunes[z] = getFortune(z)
    return fortunes
