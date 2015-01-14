
app = require('express')()

env = require('./env.coffee')
filter = require('./filter.coffee')
embedly = require('./embedly.coffee')
readability = require('./readability.coffee')

createJoin = (n, c) -> 
    (args...) ->
        if --n <= 0
            c.apply({}, args)

app.get('/', (req, res) ->
    if req.query.key isnt env.key
        console.log('ERROR: Bad key.')
        res.end('ERROR: Bad key.')
    else
        filterJoin = createJoin(2, ->
            console.log('Received sources.')
            res.end(JSON.stringify(filter(
                sources.embedly,
                sources.readability)))
            console.log('Responded.'))
        
        sources = {}
        url = req.query.url
        
        embedly(url, (obj) -> 
            sources.embedly = obj
            filterJoin())
        
        readability(url, (obj) ->
            sources.readability = obj
            filterJoin()))

port = process.env.PORT || 8004
console.log("Start app on port #{port}.")
app.listen(port)
