import telepot
import requests
import json
import random
import urllib3
import sys

if "--local" not in sys.argv:
    proxy_url = "http://proxy.server:3128"
    telepot.api._pools = {
        'default': urllib3.ProxyManager(proxy_url=proxy_url, num_pools=3,
            maxsize=10, retries=False, timeout=30),
    }
    telepot.api._onetime_pool_spec = (urllib3.ProxyManager,
        dict(proxy_url=proxy_url, num_pools=1, maxsize=1, retries=False,
            timeout=30))

cuisines = ['greek', 'southern_us', 'irish', 'mexican', 'chinese', 'filipino',
            'vietnamese', 'moroccan', 'brazilian', 'japanese', 'british',
            'indian', 'jamaican', 'french', 'spanish', 'russian', 'cajun_creole',
            'thai', 'korean', 'italian']

with open("_e3e6a884a5431c0a4f8f24f439410ce0_recipes.json") as f:
    recipes = json.load(f)

recs = {}

gr = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'greek':
        gr.append(recipes[i]['ingredients'])

recs['greek'] = gr

s_us = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'southern_us':
        s_us.append(recipes[i]['ingredients'])

recs['southern_us'] = s_us

ir = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'irish':
        ir.append(recipes[i]['ingredients'])

recs['irish'] = ir

mex = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'mexican':
        mex.append(recipes[i]['ingredients'])

recs['mexican'] = mex

chi = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'chinese':
        chi.append(recipes[i]['ingredients'])

recs['chinese'] = chi

fi = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'filipino':
        fi.append(recipes[i]['ingredients'])

recs['filipino'] = fi

vi = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'vietnamese':
        vi.append(recipes[i]['ingredients'])

recs['vietnamese'] = vi

mo = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'moroccan':
        mo.append(recipes[i]['ingredients'])

recs['moroccan'] = mo

br = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'brazilian':
        br.append(recipes[i]['ingredients'])

recs['brazilian'] = br

ja = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'japanese':
        ja.append(recipes[i]['ingredients'])

recs['japanese'] = ja

bri = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'british':
        bri.append(recipes[i]['ingredients'])

recs['british'] = bri

ind = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'indian':
        ind.append(recipes[i]['ingredients'])

recs['indian'] = ind

jam = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'jamaican':
        jam.append(recipes[i]['ingredients'])

recs['jamaican'] = jam

fre = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'french':
        fre.append(recipes[i]['ingredients'])

recs['french'] = fre

spa = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'spanish':
        spa.append(recipes[i]['ingredients'])

recs['spanish'] = spa

ru = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'russian':
        ru.append(recipes[i]['ingredients'])

recs['russian'] = ru

c_cr = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'cajun_creole':
        c_cr.append(recipes[i]['ingredients'])

recs['cajun_creole'] = c_cr

thai = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'thai':
        thai.append(recipes[i]['ingredients'])

recs['thai'] = thai

ko = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'korean':
        ko.append(recipes[i]['ingredients'])

recs['korean'] = ko

it = []
for i in range(len(recipes)):
    if recipes[i]['cuisine'] == 'italian':
        it.append(recipes[i]['ingredients'])

recs['italian'] = it

def generate_recipe(cuisine):
    r = random.choice(recs[str(cuisine)])
    return 'For this meal you will need '+', '.join(map(str, r)) + '.'


token = '857435860:AAHNKQx202gHa73Ce86e4qLz3LTT_nvcipY'
bot = telepot.Bot(token)

def reply(text, chat_id):
    if text in recs:
        bot.sendMessage(chat_id, generate_recipe(str(text)))
    else:
        bot.sendMessage(chat_id, 'Try something else!')

update_id = 0

while True:
    updates = bot.getUpdates(offset = update_id + 1)
    for update in updates:
        if update['update_id'] > update_id:
            update_id = update['update_id']
            reply(update['message']['text'], update['message']['chat']['id'])
