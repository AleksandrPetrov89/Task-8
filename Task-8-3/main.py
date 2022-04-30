import datetime
import time
import requests
from pprint import pprint
from datetime import date


def sending_request(days_ago):
    url = 'https://api.stackexchange.com//2.3/questions'
    # date_unix = int(time.time() - days_ago * 24 * 60 * 60)
    # print(date_unix)
    start_date = str(date.today() - datetime.timedelta(days=days_ago))
    date_unix = int(time.mktime(time.strptime(start_date, '%Y-%m-%d')))
    # print(date_unix)
    params = {'fromdate': date_unix, 'order': 'asc', 'sort': 'creation',
              'tagged': 'Python', 'site': 'stackoverflow', 'filter': '!)riR7Z9)aTWl.S0pGNBv'}
    resp = requests.get(url, params=params)
    data = resp.json()
    return data


if __name__ == '__main__':
    day = 2
    info = sending_request(day)
    pprint(info)
