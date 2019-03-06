#!/usr/bin/env bash
echo "Bot Id:"

read bot

echo "Access Token:"

read access

echo "Group Id:"

read group

cp envs.sh real_envs.sh

sed -i "s/\(T_ID='\)/\1$bot/; s/\(TOKEN='\)/\1$access/; s/\(P_ID='\)/\1$group/" real_envs.sh
