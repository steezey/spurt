
url = 'https://readability.com/api/content/v1/parser?token=ea3d691c39aa930e5e7e709b0f16662a03d00aeb&url='
dbName = 'gauss_readabilityresponse'

module.exports = require('./scraper.coffee')(url, dbName)