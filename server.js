var express = require('express'),
	app = express(),
	bodyParser = require('body-parser'),
	ejs = require('ejs'),
	request = require('request'),
	port = process.env.PORT || 3000,
	config = require('./config')(app.get('env')),
	knex = require('knex')(config.dbconfig),
	request = require('request'),
	_ = require('underscore'),
	S = require('string');

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({
	extended: false
}));

app.get('/', function(req, res) {
	res.send('online');
});

app.get('/items', function(req, res) {
	knex('entries')
		.orderBy('entries.id', 'desc')
		.leftJoin('items', 'entries.item_id', 'items.id')
		.select('*', 'entries.id')
		.then(function(items) {
			var filtered = _.map(items, function(item) {
				return {
					id: item.id,
					title: item.title,
					content: S(item.content).stripTags().s,
					source: item.provider_name
				};
			});
			res.send(filtered);
		});
});

app.post('/item', function(req, res) {
	var url = req.body.url;
	var encodedurl = encodeURIComponent(url);

	var embedlyurl = 'http://api.embed.ly/1/extract?key='+config.embedly.key+'&url='+encodedurl;
	knex('items').where('original_url', url).first().then(function(item) {
		if (item) {
			knex('entries').insert({
				item_id: item.id
			}).then(function() {
				res.send('done');
			});
		} else {
			request.get(embedlyurl, function(error, response, body) {
				body = JSON.parse(body);
				var insertObj = {
					title: body.title || '',
					published: body.published,
					url: body.url || '',
					content: body.content || '',
					original_url: body.original_url || '',
					description: body.description || '',
					provider_name: body.provider_name || ''
				};
				knex('items').insert(insertObj).then(function(inserted) {
					var id = inserted[0];
					knex('entries').insert({
						item_id: id
					}).then(function() {
						res.send('success');
					});
				});
			});
		}
	});
});

app.post('/swap', function(req, res) {
    var authCode = req.param('code');
    // request.debug = true;
    request.post({
    	uri: config.SPT_TOKEN_ENDPOINT,
    	headers: {
    		"Authorization": config.SPT_AUTH_HEADER
    	},
    	form: {
	        grant_type: 'authorization_code',
	        redirect_uri: config.SPT_CLIENT_CALLBACK_URL,
	        code: authCode
    	},
    	json: true
    }, function(error, response, body) {
    	if(response.statusCode == 200) {
    		//should symmetrically encrypt refresh_token before forwarding to client
    	}

    	res.status(response.statusCode).send(body);
    });
});

app.listen(port);
console.log('Serving on port ' + port);