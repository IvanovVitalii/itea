import urllib.request
import urllib.parse
from urllib.parse import quote

from bs4 import BeautifulSoup

URL = 'https://sinoptik.ua'


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def parse(html):
    soup = BeautifulSoup(html, features='html.parser')
    week = soup.find('div', class_='tabs')
    days = week.find_all('div', class_='main')

    forecast = []
    for day in days:
        date = day.find_all('p')

        weather = day.find_all('div')
        temperature = weather[1].find_all('div')


        forecast.append({
            'day': date[0].text,
            'date': date[1].text,
            'month': date[2].text,
            'weather': weather[0]['title'],
            'min_temperature': temperature[0].text,
            'max_temperature': temperature[1].text
        })
    return forecast


def get_weather_data(z, day, town=None):
    list_weather = []
    for i in z:
        l = list(i.values())
        if day in l:
            list_weather = l
    return list_weather



def main():

    city = f'погода-{input("введите город")}'
    city = quote(city)
    print(city)


    a = get_html(URL)
    z = parse(a)
    day = input('day:')
    y = get_weather_data(z, day)
    for i in y:
        print(i)





if __name__ == '__main__':
    main()
