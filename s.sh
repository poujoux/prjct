#!/bin/bash

read -p "message" message

git add .
git commit -m "$message"
git push 

sleep 30
echo "....."

gh run view --log

