#/usr/bin/env bash

pip install pylint bandit

output=$(python3 -m pylint --errors-only app/app.py)
status=0
if [ -n "$output" ]; then
    status=1
else
    status=0
fi
output=$(python3 -m bandit -r app/. -lll -q)
if [ -n "$output" ]; then
    status=1
else
    status=0
fi
