ok will, here we go, iteratation 2

API modifications:
posts can be either text or link posts (text posts cannot be saved as drafts in the inbox, while link posts can be saved in the inbox)
posts have comments which may each further have subcomments (for now no deleting any comments)

about what mysql field each parameter should take, you decide

new endpoints:
make a new link post (skip saving to inbox first)
	- udid
	- link
	- title
	- description
make a new text post
	- udid
	- title
	- content
create comment
	- parentid (optional)