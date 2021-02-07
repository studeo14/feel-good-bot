#!/usr/bin/env bash
source ./real_envs.sh || source ./scripts/real_envs.sh
python3 src/notify.py "$@"
