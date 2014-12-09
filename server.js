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

	// res.send('lets show them');
	// knex('items').insert
});

app.listen(port);
console.log('Serving on port ' + port);