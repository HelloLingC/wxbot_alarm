from wxpy import *
import time
import requests

bot = None

def bot_login():
    global bot
    if bot == None:
        bot = Bot()
    return bot

def iyan_ask():
    url = 'https://v1.hitokoto.cn/'
    request = requests.get(url)
    reson = request.json()
    return reson

def alarm(hour, minute):
    bot = bot_login()
    friends = bot.friends()
    groups = bot.groups()
    group1 = groups.search('ID1')[0]
    group2 = groups.search('ID2')[0]
    while True:
        ti = time.localtime()
        h, m = ti[3:5]
        if hour == h and minute == m:
             iyan = iyan_ask()
             text = '现在是{} : {}。\n{}\nFrom {}'.format(h, m, iyan['hitokoto'], iyan['from'])
             print(text)
             group1.send(text)
             group2.send(text)
             break
        time.sleep(1)

if __name__ == '__main__':
    ti = time.localtime()[3:4][0] # 截取小时
    while True:
        ti += 1
        alarm(ti, 30)
        time.sleep(100)