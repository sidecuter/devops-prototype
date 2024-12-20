#/usr/bin/env bash

echo "Executing linter"
output=$(python3 -m pylint --errors-only app/app.py)
status=0
if [ -n "$output" ]; then
    status=1
    echo "Linting failed"
else
    status=0
    echo "Linting success"
fi
echo "Executing bandit"
output=$(python3 -m bandit -r app/. -lll -q)
if [ $status -eq 1 ]; then
    exit $status
fi
if [ -n "$output" ]; then
    echo "bandit failed"
    status=1
else
    echo "Bandit success"
    status=0
fi
exit $status
