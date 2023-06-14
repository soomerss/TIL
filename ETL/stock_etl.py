import pandas as pd
import requests
import json
from datetime import date, timedelta

def get_df(date):
    key = key
    url = f"https://apis.data.go.kr/1160100/service/GetStockSecuritiesInfoService/getStockPriceInfo?serviceKey={key}&basDt={date}&resultType=json&numOfRows=10000&pageNo=1"
    req = requests.get(url)
    json_file = json.loads(req.text)
    parse_file = json_file['response']['body']['items']
    df = pd.json_normalize(parse_file['item'])
    return df


total_days = []
day = timedelta(days=1)
start_day = date(2023, 6, 1)
while start_day <= date.today():
    add_day = start_day.strftime('%Y%m%d')
    print(add_day)
    total_days.append(add_day)
    start_day += day


def make_large_date(total_days):
    for i in total_days:
        if i == '20230601':
            df = get_df(i)
        else :
            df = pd.concat([df,get_df(i)],ignore_index=True)
    return df