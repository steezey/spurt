// Update with your config settings.

module.exports = {
  development: {
    client: 'mysql',
    connection: {
      host: 'localhost',
      user: "root",
      password: "root",
      database: "spikedb"
    },
    migrations: {
      tableName: 'migrations'
    }
  },
  production: {
    client: 'mysql',
    connection: {
      host: "restore.cdy2lzrsyzbw.us-west-1.rds.amazonaws.com",
      user: "chakakhan",
      password: "rootfinch",
      database: "spikedb"
    },
    migrations: {
      tableName: 'migrations'
    }
  }
};