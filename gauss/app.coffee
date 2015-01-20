
assert = require('assert')
app = require('express')()
request = require('request')

env = require('./env.coffee')
filter = require('./filter.coffee')
embedly = require('./embedly.coffee')
readability = require('./readability.coffee')

createJoin = (n, c) -> 
    (args...) ->
        if --n <= 0
            c.apply({}, args)

app.get('/', (req, res) ->
    console.log(req.query)
    if req.query.key isnt env.key
        console.log('ERROR: Bad key.')
        res.end('ERROR: Bad key.\n')
    else
        joinFilter = createJoin(3, ->
            console.log('Received sources.')
            res.end(JSON.stringify(filter(
                sources.embedly,
                sources.readability,
                sources.page)))
            console.log('Responded.'))
        
        sources = {}
        url = decodeURIComponent(req.query.url)
        
        console.log(url)
        
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
