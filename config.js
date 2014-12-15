module.exports = function(env) {
	var config = {};

	config.embedly = {
		key: '2349d9cd48b64d988389fb4af2792a45'
	}

	config.dbconfig = env == 'development' ? {
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

	config.SPT_CLIENT_ID = "a1428c8b9add4fa68b5a5668d48e0b87";
	config.SPT_CLIENT_SECRET = "369f4121a58347d9a20827cd5ee0e3a7";
	config.SPT_ENCRYPTION_SECRET = "cFJLyifeUJUBFWdHzVbykfDmPHtLKLGzViHW9aHGmyTLD8hGXC";
	config.SPT_CLIENT_CALLBACK_URL = "spotifybeginner://callback";
	config.SPT_AUTH_HEADER = "Basic " + new Buffer(config.SPT_CLIENT_ID + ":" + config.SPT_CLIENT_SECRET).toString('base64');
	config.SPT_TOKEN_ENDPOINT = "https://accounts.spotify.com/api/token";

	return config;
}