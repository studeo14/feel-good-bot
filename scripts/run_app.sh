#!/usr/bin/env bash
source ./real_envs.sh || source ./scripts/real_envs.sh
cd src
gunicorn -b 0.0.0.0:8000 app:app
