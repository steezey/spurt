
# echo 'Starting servers...'

# # Start spurt

# ./manage.py runserver &

# PIDS[0]=$!

# # Start gauss

# node gauss/server.js &

# PIDS[1]=$!

# sleep 3

# echo 'Servers started.'

# link-posts/create-and-publish --data

curl localhost:8000/link-posts/create-and-publish --data "uuid=test_uuid&url=http://www.youtube.com&title=test_title&description=test_description"

curl localhost:8000/link-posts/create --data "uuid=test_uuid&url=http://www.youtube.com"

curl localhost:8000/auth-code?uuid=test_uuid


# trap "kill ${PIDS[*]}" SIGINT

# wait
