
knex = require('./knex.coffee')
request = require('request')

module.exports = (scraperURL, dbName) -> 
    knex
        .schema
        .hasTable(dbName)
        .then((exists) ->
            if not exists
                knex.schema.createTable(dbName, (table) ->
                    table.text('url')
                    table.text('response')))
    
    (url, callback) ->
        knex
            .select('response')
            .from(dbName)
            .where(url: url)
            .then((objs) ->
                if 0 < objs.length
                    callback(JSON.parse(objs[0].response))
                else
                    request(scraperURL + url,
                        (error, res, body) ->
                            if not error
                                callback(JSON.parse(body))
                                knex
                                    .insert(
                                        url: url
                                        response: body)
                                    .into(dbName)
                                    .return()
                            else
                                throw error))
