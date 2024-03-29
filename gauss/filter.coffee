
_ = require('customscore')
$ = require('jquery')(require('jsdom').jsdom().parentWindow)
sanitizeHtml = require('sanitize-html')

REGEX = 
    DATE: /^[0-9]{4}/

module.exports = (e, r, html) ->
    # For docs, see scraping-methodology.md.
    
    scraped = 
        scraped_title: e.title or r.title
        
        domain: r.domain or e.provider_display
        
        original_url: e.original_url or url
        
        url: r.url or e.url or url
        
        rddme_url: r.short_url
        
        provider_name: e.provider_name
        
        author_name: r.author or (e.authors[0] ? {}).name
        
        authors: JSON.stringify(
            if 0 < e.authors.length then e.authors else if r.author then [{name: r.author}] else [])
        
        dek: e.description or r.dek
        
        lead: r.excerpt or e.lead
        
        lead_image: r.lead_image_url
        
        safe: e.safe
        
        favicon: e.favicon_url
    
    pub_date = r.date_published or e.published
    
    if pub_date? and pub_date.match(REGEX.DATE)
        scraped.scraped_pub_date = pub_date
    
    ###
    
    The content field is special. We set it according to the following pattern:
    If e.media is set:
        Set content and content_filtered equal to the simplest block of html that contains the photo, video, or "rich" html document.
    Otherwise:
        Set content to r.content, e.content.
        Set content_filtered to the paragraph and image elements of content.

    ###
    
    if e.media isnt undefined and e.media.type isnt undefined
        if e.media.type is 'photo'
            scraped.content = "<img src='#{e.media.url}>"
        else if e.media.type is 'video'
            $('body').html(e.media.html)
            $('iframe.embedly-embed').map((i, e) ->
                $(e).attr('src', 'http:' + $(e).attr('src')))
            scraped.content = $('body').html()
        else
            scraped.content = e.media.html
        scraped.content_filtered = scraped.content
    else
        scraped.content = r.content or e.content or html
        if scraped.content?
            TAGS_TO_SCRAPE = 'p img h1 h2 h3 h4 h5 h6'.split(' ')
            
            scraped.content_filtered = sanitizeHtml(
                scraped.content,
                allowedTags: TAGS_TO_SCRAPE)
    
    return scraped
