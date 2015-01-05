
Bugs:
-------- Saving http://www.smithsonianmag.com/?no-ist stores no favicon_url, when the embedly call provides it
-------- Inbox posts are in reverse order
-------- Text posts content is always empty. description is not saving (this is because the database field name is "content")

Requests:
---- Output url_content & url_content_filtered in both the public and inbox routes
-------- Differentiation field for posts to distinguish text from link posts (type?) in the public output
---- text-post & link-post /publish accept title and description so you edit the post and publish it at the same time
-------- Link posts include the published parameter from embedly and output this
---- Link posts include the content from embedly (this has html tags in it, but I need it cleaned up with no html tags and with an \n in between every paragraph) and output this
---- Lastly, cache all embedly requests. You can do this by making a separate table. The reason why is because of request speed (a lot faster to serve cached values), and also because embedly calls can cost a lot.