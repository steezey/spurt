Todo & Errors:
- the media html should not be its own json field. it should be displayed in the content field of output (esp. for youtube) if the content is empty. you have to make these decisions logically - we want the best data outputted to the user and an empty content is always worse than outputting the media html as the content.

ERROR - saving [https://m.youtube.com/watch?v=1cuu0I7oZWU] gives an author of "{u'url': u'http://www.youtube.com/user/joonpoo', u'name': u'Joon Lee'}"

- embedly has weaknesses (esp. with the author field which is almost always empty and sometimes the content & media). [http://nymag.com/daily/intelligencer/2014/12/genius-minus-the-rap.html] returns empty author and content in embedly, but has an author and content with other scraping services. For example with the Readability API (https://readability.com/api/content/v1/parser?url=http://nymag.com/daily/intelligencer/2014/12/genius-minus-the-rap.html&token=ea3d691c39aa930e5e7e709b0f16662a03d00aeb) the author is supplied and the content is supplied. There are too many inaccuracies with embedly, so we must supplement it with others. The choice of how to improve our API is yours, but I suggest using the Readability API (and our API token is ea3d691c39aa930e5e7e709b0f16662a03d00aeb) to cover any empty fields that embedly may have for a page. And then the Readability API call is asynchronous (meaning the user doesnt have to wait for both embedly AND readability), but readability runs in the background after embedly. Again, the choice is yours, just the end result is that we get the best data and it is fast on the user end.


- save http://www.washingtonpost.com/local/virginia-politics/robert-f-mcdonnell-sentenced-to-two-years-in-prison-in-corruption-case/2015/01/06/e51520ca-9049-11e4-ba53-a477d66580ed_story.html?tid=HP_lede?tid=HP_lede
- url_title null error https://www.youtube.com/watch?v=6XSEi1jTR58
- something about media field (see slack)