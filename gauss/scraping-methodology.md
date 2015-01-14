
Result
======

The resulting object has the following fields:

scraped_title
domain
original_url
url
rddme_url
author_name
author
dek
lead
lead_image
pub_date
embedly_safe
favicon
content

Readability
======

Readability provides the following fields. When readability fails to assign values to a field, it leaves the field in the json but sets it to null.

domain
next_page_id
url
short_url
author
excerpt
direction
word_count
total_pages
content
date_published
dek
lead_image_url
title
rendered_pages

Embedly
======

original_url
url
type
cache_age
safe
provider_name
provider_url
provider_display
favicon_url
favicon_colors
title - not just the html element
authors
published - date published
offset - UTC offset of date published
description - meta, or else embedly pulls programmatically
lead - the first lines of the article in the form of a p tag

content - sanitized content
media
    photo
        url
        width
        height
    video
        html - load in off-domain iframe?
        width
        height
    "rich"
        html
        width
        height

keywords
entities
related
images

Readability Fields Used
======

domain
url
short_url
author
excerpt
content
date_published
dek
lead_image_url
title

Embedly Fields Used
======

original_url
url
safe
provider_name
provider_url
provider_display
favicon_url
favicon_colors
title - not just the html element
authors
published - date published
offset - UTC offset of date published
description - meta, or else embedly pulls programmatically
lead - the first lines of the article in the form of a p tag

content - sanitized content
media
    photo
        url
        width
        height
    video
        html - load in off-domain iframe?
        width
        height
    "rich"
        html
        width
        height

Methodology
======

Except for the "content" and "content_filtered" fields, we take all fields directly from embedly, readability, or the given url. The following lists each field followed by a dash a comma-separated list of fields we search for the value. Fields from embedly are written "e.field_name" and fields from readability are written "r.field_name".

scraped_title - e.title, r.title

domain - r.domain, e.provider_display

original_url - e.original_url, url

url - r.url, e.url, url

rddme_url - r.short_url

author_name - r.author, e.authors[0].name

author - e.author, {name: r.author}

dek - e.description, r.dek

lead - r.excerpt, e.lead

lead_image - r.lead_image_url

pub_date - r.date_published, e.published

embedly_safe - e.safe

favicon - e.favicon_url

The content field is special. We set it according to the following pattern:

If e.media is set:
    Set content and content_filtered equal to the simplest block of html that contains the photo, video, or "rich" html document.
Otherwise:
    Set content to r.content, e.content.
    Set content_filtered to the paragraph and image elements of content.
