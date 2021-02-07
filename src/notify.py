#! /usr/bin/env python3

# IMPORTS
import os
import sys
import json
import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from tinydb import TinyDB, Query
from tinydb.operations import increment
from utils import get_members, reply
import schedule

bot_id = os.environ['BOT_ID']
access_token = os.environ['ACCESS_TOKEN']
group_id = os.environ['GROUP_ID']
crown = '👑'


# Send a message in the groupchat

def read_leaderboard():
    url = 'https://api.groupme.com/v3/groups/{}/likes?period=day&token={}'.format(group_id, access_token)
    print('Getting leaderboard from {}', url)
    request = Request(url)
    body = json.loads(urlopen(request).read().decode())
    return body['response']

def find_top_poster(leaderboard):
    if len(leaderboard['messages']) == 0:
        return None
    else:
        top_message = None
        top_message_likes = 0
        for message in leaderboard['messages']:
            likes = len(message['favorited_by'])
            if likes > top_message_likes:
                top_message_likes = likes
                top_message = message
            elif likes == top_message_likes:
                if type(top_message) is list:
                    top_message.append(message)
                else:
                    top_message = [top_message, message]
        # extract user_ids
        if type(top_message) is list:
            uids = [m['user_id'] for m in top_message]
        else:
            uids = [top_message['user_id']]
        return (uids, top_message_likes) 
def notify_chat(top_posters):
    if top_posters is None:
        pass
    else:
        members = get_members(group_id, access_token)
        members = [member for member in members if member['user_id'] in top_posters[0]]
        if len(members) == 1:
            member = members[0]
            message = '{} had the top post yesterday with {} likes!'.format(member['nickname'], top_posters[1])
            reply(message, bot_id)
        elif len(members) > 1:
            nicks = [m['nickname'] for m in members]
            nicks = '\n'.join(nicks)
            message = 'These members tied for the top post yesterday with {} likes!\n{}'.format(top_posters[1], nicks)
            reply(message, bot_id)

def add_stars(top_poster):
    db = TinyDB('./data/db.json')
    User = Query()
    if top_poster is not None:
        for poster in top_poster[0]:
            if db.contains(User.uid == poster):
                db.update(increment('stars'), User.uid == poster)
            else:
                db.insert({'uid': poster, 'stars': 1})

def notify():
    # read leaderboard using access token
    # find top poster (post with highest # of likes)
    # tell the chat who the top poster is as the bot
    leaderboard = read_leaderboard()
    top_poster = find_top_poster(leaderboard)
    notify_chat(top_poster)
    add_stars(top_poster)


if __name__ == '__main__':
    notify()
