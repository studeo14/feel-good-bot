#!/usr/bin/env bash
source ./real_envs.sh
python3 -m gunicorn -b 0.0.0.0:8000 app:app
