from django.test import TestCase
from django.db import models
import datetime

# 賞味・消費期限通知機能

msg_list = []
five_days = datetime.timedelta(days=5)
zero_days = datetime.timedelta(days=0)
today = datetime.date.today()
day = '2024-6-21'

# 文字列の日付をdatetime.date型に変換
if day is not None:
    day_date = datetime.datetime.strptime(day, '%Y-%m-%d').date()
    delta = day_date - today
    print(delta)
