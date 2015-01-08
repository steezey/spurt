
require('http').Server((req, res) ->
    res.end('hello')).listen(8000)