
url = 'http://api.embed.ly/1/extract?key=2349d9cd48b64d988389fb4af2792a45&url='
dbName = 'gauss_embedlyresponse'

module.exports = require('./scraper.coffee')(url, dbName)
