#!/usr/bin/env bash
source ./real_envs.sh || source ./scripts/real_envs.sh
/usr/bin/env python3 src/notify.py "$@"
