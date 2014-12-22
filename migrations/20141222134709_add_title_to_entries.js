'use strict';

exports.up = function(knex, Promise) {
	return Promise.all([
		knex.schema.table('entries', function(table) {
			table.string('title', 510);
		})
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.table('entries', function(table) {
			table.dropColumn('title');
		})
	]);
};
