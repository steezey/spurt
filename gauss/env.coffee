
os = require('os')

exports.isProd = os.hostname() isnt '4.local' and os.hostname() isnt '4-6.local'

if exports.isProd
    console.log('Running in PROD')
else
    console.log('Running in DEV')

exports.key = '4a9fdf362ffff48fc64f2c3621166a75'

exports.url = {}
    

if exports.isProd
    exports.url.receive_scrape = 'http://spurt.elasticbeanstalk.com/link-posts/receive-scrape'
else
    exports.url.receive_scrape = 'http://localhost:8000/link-posts/receive-scrape'