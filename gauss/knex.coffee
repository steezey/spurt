
env = require('./env.coffee')

if env.isProd
    module.exports = require('knex')
        client: 'mysql'
        connection:
            host: 'restore.cdy2lzrsyzbw.us-west-1.rds.amazonaws.com',
            user: 'chakakhan',
            password: 'rootfinch',
            database: 'spurt'
            port: 3306 # TODO: do I need this?
else
    module.exports = require('knex')
        client: 'sqlite3'
        connection:
            filename: "../db.sqlite3"