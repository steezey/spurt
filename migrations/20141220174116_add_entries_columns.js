'use strict';

exports.up = function(knex, Promise) {
	return Promise.all([
		knex.schema.table('items', function(table) {
			table.string('provider_display');
			table.string('favicon_url', 510);
		})
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.table('items', function(table) {
			table.dropColumn('provider_display');
			table.dropColumn('favicon_url');
		})
	]);
};
