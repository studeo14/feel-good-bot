# feel-good-bot
## What is this?
A GroupMe bot that comes in two parts:
1. `app.py`: callback-style bot that can give the requester an all-time leaderboard
2. `notify.py`: job-style bot that sends a message to the group about who was the 'best' poster of the previous day.

## How to use?
1. Modify `env.sh` to hold values that are appropriate to you and your group
2. Install deps with `pip install -r requirements.txt`
3. Schedule `notify.py` with a job manager like cron
4. Run `app.py`

## Upcoming Features
- Implement `app.py`
 - Look for trigger (configurable?) and reply with list of `name`:`star count`
 - Database read
- Dockerize
