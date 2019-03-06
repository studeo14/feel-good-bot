#!/usr/bin/env bash
source ./real_envs.sh
gunicorn -b 0.0.0.0:8000 app:app
