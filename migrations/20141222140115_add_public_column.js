'use strict';

exports.up = function(knex, Promise) {
	return Promise.all([
		knex.schema.table('entries', function(table) {
			table.boolean('public');
		})
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.table('entries', function(table) {
			table.dropColumn('public');
		})
	]);
};
