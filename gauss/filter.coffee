
_ = require('customscore')
$ = require('jquery')(require('jsdom').jsdom().parentWindow)

module.exports = (e, r) ->
    # For docs, see scraping-methodology.md.
    
    scraped = 
        title: e.title or r.title

        domain: r.domain or e.provider_display

        original_url: e.original_url or url

        url: r.url or e.url or url

        rddme_url: r.short_url

        author_name: r.author or (e.authors[0] ? {}).name

        author: e.author or {name: r.author}

        dek: e.description or r.dek

        lead: r.excerpt or e.lead

        lead_image: r.lead_image_url

        pub_date: r.date_published or e.published

        safe: e.safe

        favicon: e.favicon_url

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
        else
            scraped.content = e.media.html
        scraped.content_filtered = scraped.content
    else
        scraped.content = r.content or e.content
        if scraped.content?
            TAGS_TO_SCRAPE = 'p img h1 h2 h3 h4 h5 h6'.split(' ')
            
            $('body').html(scraped.content)
            tags = $(TAGS_TO_SCRAPE.join(', '))
            
            scraped.content_filtered = _.chain(tags)
                    .pluck('outerHTML')
                    .value()
                    .join('')
    
    return scraped
