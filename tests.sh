
curl localhost:8000/link-posts/create-and-publish --data "uuid=test_uuid&url=http://www.youtube.com&title=test_title&description=test_description"

curl localhost:8000/link-posts/create --data "uuid=test_uuid&url=http://www.youtube.com"

curl localhost:8000/auth-code?uuid=test_uuid

curl localhost:8000/posts/public > temp/tests/public.html && open temp/tests/public.html

curl localhost:8000/posts/inbox?uuid=test_uuid > temp/tests/inbox.html && open temp/tests/inbox.html