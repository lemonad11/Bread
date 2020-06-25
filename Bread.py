import json
import csv
import datetime
from idlelib.multicall import r
from time import sleep
import requests
data = ["время, код ответа, задержка".split(","),]


for i in range(100):
    d = datetime.datetime.now()
    result = requests.get('http://www.yandex.ru/', timeout=60)
    speed = result.elapsed.total_seconds()
    code = result.status_code
    print(d)
    print(code, end="  задержка = ")
    print(speed)
    data.append([d, code, speed])
    #sleep(3)


def csv_writer(data, path):
    with open(path, "w", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)


path = "My internet.csv"
csv_writer(data, path)

