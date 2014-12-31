
Will: debug API v2
Austin: Change frontend API calls
    - items/public -> posts/public
    - items/inbox -> posts/inbox
    - items/create -> link-posts/create
    - items/edit -> link-posts/edit
    - items/publish -> link-posts/publish


Bugs:
- Saving http://www.smithsonianmag.com/?no-ist stores no favicon_url, when the embedly call provides it
- Inbox posts are in reverse order