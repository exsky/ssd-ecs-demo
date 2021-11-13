import aiohttp
import asyncio
import requests
from bs4 import BeautifulSoup


async def getFortune(what, session):
    if not what:
        url = "https://www.daily-zodiac.com/mobile/zodiac/Aries"
    else:
        url = "https://www.daily-zodiac.com/mobile/zodiac/{}".format(what)
    try:
        async with session.get(url=url) as response:
            resp = await response.read()
            soup = BeautifulSoup(resp, "html.parser")
            result = soup.find("article").getText()
            result = result.replace('\n', '')
            result = result.replace(' ', '')
    except Error as e:
        print(e)
    return result


async def get_12_horo():
    fortunes = {}
    zodiac = [ 'Aries', 'Taurus', 'Gemini', 'Cancer',
               'Leo', 'Virgo', 'Libra', 'Scorpio',
               'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces'
               ]
    async with aiohttp.ClientSession() as session:
        ret = await asyncio.gather(*[getFortune(z, session) for z in zodiac])
        for z in zodiac:
            fortunes[z] = ret[zodiac.index(z)]
    return fortunes
