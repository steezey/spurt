Todo & Errors:
- the media html should not be its own json field. it should be displayed in the content field of output (esp. for youtube) if the content is empty. you make the decisions logically - we want the best data outputted to the user, so we lets output the media output instead of nothing. the content field is being shown to the user, the FE isn't deciding between showing 'content' and 'media' - all the logic for deciding which html the user should see should be done in the backend and outputted in the content field.

ERROR - saving [https://m.youtube.com/watch?v=1cuu0I7oZWU] gives an author of "{u'url': u'http://www.youtube.com/user/joonpoo', u'name': u'Joon Lee'}". On second thought, all articles that have author supplied are being saved incorrectly. 1) Please refer to resources that can help you build out to requirements: http://embed.ly/docs/explore/extract?url=http%3A%2F%2Fwww.businessinsider.com%2Frap-genius-co-founder-blasts-his-former-partners-2015-1 2) You definitely should test new features of your API at LEAST once - no author field is being saved correctly. there is no rush for you to slack me that it's done, you can take extra time - all the time you need - to be confident in it

- embedly has weaknesses (esp. with the author field which is almost always empty and sometimes the content & media). [http://nymag.com/daily/intelligencer/2014/12/genius-minus-the-rap.html] returns empty author and content in embedly, but has an author and content with other scraping services. For example with the Readability API (https://readability.com/api/content/v1/parser?url=http://nymag.com/daily/intelligencer/2014/12/genius-minus-the-rap.html&token=ea3d691c39aa930e5e7e709b0f16662a03d00aeb) the author is supplied and the content is supplied. There are too many inaccuracies with embedly, so we must supplement it with others. The choice of how to improve our API is yours, but I suggest using the Readability API asynchronously (our API token is ea3d691c39aa930e5e7e709b0f16662a03d00aeb) to cover any empty fields that embedly may have for a page. Readability API call is asynchronous so the user doesnt have to wait for both embedly AND readability. so the readability call runs in the background after embedly (we simply can't have the user wait for two synchronous requests (~5secs). Again, the choice is yours, just the end result is that we get the best data and it is fast on the user end.
(some more resources: http://fivefilters.org/content-only/, http://stackoverflow.com/questions/5960948/how-to-extract-text-contents-from-html-like-read-it-later-or-instapaper-iphone-a)

ERROR - saving [https://m.youtube.com/watch?v=1cuu0I7oZWU] gives an author of "{u'url': u'http://www.youtube.com/user/joonpoo', u'name': u'Joon Lee'}"

- ask me for clarification and i will get back to you, please ask anything that is ambiguous to you



Will's notes
- save http://www.washingtonpost.com/local/virginia-politics/robert-f-mcdonnell-sentenced-to-two-years-in-prison-in-corruption-case/2015/01/06/e51520ca-9049-11e4-ba53-a477d66580ed_story.html?tid=HP_lede?tid=HP_lede
- url_title null error https://www.youtube.com/watch?v=6XSEi1jTR58
- something about media field (see slack)