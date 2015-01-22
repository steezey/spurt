
echo 'Starting node...'

node gauss/server.js &

PIDS[0]=$!

echo 'Running tests...'

./manage.py 'test'

trap "kill ${PIDS[*]}" SIGINT

wait
