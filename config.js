module.exports = function(env) {
	var config = {};

	config.embedly = {
		key: '2349d9cd48b64d988389fb4af2792a45'
	}

	config.dbconfig = env == 'development' ?
		{
			client: 'mysql',
			connection: {
				host: 'localhost',
				user: "root",
				password: "root",
				database: "spikedb"
			}
		} : {
			client: 'mysql',
			connection: {
				host: "restore.cdy2lzrsyzbw.us-west-1.rds.amazonaws.com",
				user: "chakakhan",
				password: "rootfinch",
				database: "spikedb"
			}
		};

	return config;
}