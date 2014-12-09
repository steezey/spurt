'use strict';

exports.up = function(knex, Promise) {
	return Promise.all([
		knex.schema.createTable('entries', function(table) {
			table.increments();
			table.integer('item_id').unsigned();
		})
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.dropTable('entries')
	]);
};
