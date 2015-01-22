
assert = require('assert')
app = require('express')()
request = require('request')
_ = require('customscore')

env = require('./env.coffee')
filter = require('./filter.coffee')
embedly = require('./embedly.coffee')
readability = require('./readability.coffee')

createJoin = (n, c) -> 
    (args...) ->
        if --n <= 0
            c.apply({}, args)

error = (res, message) ->
    console.log('ERROR: ' + message)
    res.end('ERROR: ' + message + '\n')

app.get('/', (req, res) ->
    console.log('Received request: ' + req.url)
    if req.query.key isnt env.key
        error(res, 'Bad key.')
    else
        undefinedKeys = ['scrape_token', 'url'].filter((key) -> 
            req.query[key] is undefined)
        if 0 < undefinedKeys.length
            error(res, 'No ' + undefinedKeys.join(' or '))
        else
            res.end(JSON.stringify({message: 'Received'}))
            joinFilter = createJoin(3, ->
                console.log('Received sources.')
                scraped = _.extend(
                    {scrape_token: req.query.scrape_token},
                    filter(
                        sources.embedly,
                        sources.readability,
                        sources.page))
                console.log(scraped)
                request.post(
                    env.url.receive_scrape,
                    form: scraped)
                console.log('Responded.'))
            
            sources = {}
            url = decodeURIComponent(req.query.url)
            
            embedly(url, (obj) -> 
                sources.embedly = obj
                joinFilter())
            
            readability(url, (obj) ->
                sources.readability = obj
                joinFilter())
            
            request(url, (error, res, body) ->
                assert.ifError(error)
                console.log(body[0...100])
                sources.page = body
                joinFilter()))

port = process.env.PORT || 8004
console.log("Start app on port #{port}.")
app.listen(port)
