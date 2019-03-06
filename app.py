import os
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from tinydb import TinyDB, Query
from tinydb.operations import increment
from flask import Flask, request
from utils import get_members, reply

app = Flask(__name__)

bot_id = os.environ['BOT_ID']
access_token = os.environ['ACCESS_TOKEN']
group_id = os.environ['GROUP_ID']

BOT_NAME = '@FeelGoodBot'

def is_request(message):
    return BOT_NAME in message['text']

def read_from_db():
    db = TinyDB('./db.json')
    leaders = db.all()
    return leaders

def ids_to_names(leaders):
    members = get_members(group_id, access_token)
    mim = {member['user_id']: member['nickname'] for member in members}
    return [{**leader, 'name': mim[leader['uid']]} for leader in leaders]

def send_leaderboard(message):
    recip = message['name']
    leaders = read_from_db()
    leaders = ids_to_names(leaders)
    leaders_stats_string = ''
    for leader in leaders:
        leaders_stats_string += '{}: {}'.format(leader['name'], leader['stars'])
    message = "@{}\nAll time stats:\n{}".format(recip, leaders_stats_string)
    reply(message, bot_id)

@app.route('/', methods=['POST'])
def webhook():
    message = request.get_json()
    print("Got message")
    if is_request(message):
        print("Got request")
        send_leaderboard(message)

    return "ok", 200
