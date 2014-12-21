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

function cleanProviderDisplay(display) {
	if (display.indexOf('www.') === 0) {
		return display.slice(4);
	}
	return display;
}

function cleanContent(content) {
	return S(content).stripTags().s
}

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
		.leftJoin('boards', 'entries.board_id', 'boards.id')
		.select('*', 'entries.id', 'boards.color')
		.then(function(items) {
			var filtered = _.map(items, function(item) {
				return {
					id: item.id.toString(),
					url: item.url,
					color: item.color,
					title: item.title,
					content: cleanContent(item.content),
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
			var data = {
				id: item.id.toString(),
				title: item.title,
				content: cleanContent(item.content) || item.description,
				provider_display: cleanProviderDisplay(item.provider_display)
			}
			res.send(data);
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
					provider_name: body.provider_name || '',
					provider_display: body.provider_display || '',
					favicon_url: body.favicon_url || ''
				};
				knex('items').insert(insertObj).then(function(inserted) {
					var id = inserted[0];
					var data = {
						id: id.toString(),
						title: insertObj.title,
						content: cleanContent(insertObj.content) || insertObj.description,
						provider_display: cleanProviderDisplay(insertObj.provider_display)
					}
					res.send(data);
				});
			});
		}
	});
});

app.post('/entry', function(req, res) {
	var item_id = req.body.item_id;
	if (!item_id) {
		res.status(500).send({error: 'something wrong happened'});
		return;
	}

	knex('items').where('id', item_id).first().then(function(item) {
		if (item) {
			knex('entries').insert({
				item_id: item.id,
				board_id: 1
			}).then(function() {
				res.send('success');
			});
		} else {
			res.status(500).send({error: 'something wrong happened'});
		}
	});
})

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