'use strict';

exports.up = function(knex, Promise) {
	return Promise.all([
		knex.schema.createTable('items', function(table) {
			table.increments();
			table.string('title', 510);
			table.bigInteger('published');
			table.string('url', 510);
			table.text('content', 'mediumtext');
			table.string('original_url', 510);
			table.string('description', 1020);
			table.string('provider_name');
		})
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.dropTable('items')
	]);
};
