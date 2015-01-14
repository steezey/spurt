
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
        res.end('ERROR: Bad key.')
    
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

app.listen(8004)
