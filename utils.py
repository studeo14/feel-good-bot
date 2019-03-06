
import json
from urllib.parse import urlencode
from urllib.request import Request, urlopen

def reply(msg, bot_id):
    url = 'https://api.groupme.com/v3/bots/post'
    data = {'bot_id': bot_id, 'text': msg}
    request = Request(url, urlencode(data).encode())
    body = urlopen(request).read().decode()

def get_members(group_id, access_token):
    url = 'https://api.groupme.com/v3/groups/{}?token={}'.format(group_id, access_token)
    request = Request(url)
    group = json.loads(urlopen(request).read().decode())['response']
    return group['members']
