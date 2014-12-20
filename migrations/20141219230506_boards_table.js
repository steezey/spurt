'use strict';

exports.up = function(knex, Promise) {
	Promise.all([
		knex.schema.createTable('boards', function(table) {
			table.increments();
			table.string('name');
			table.string('color', 6);
		}),
		knex.schema.table('entries', function(table) {
			table.integer('board_id').unsigned();
		}),
		knex.seed.run('first_boards')
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.dropTable('boards'),
		knex.schema.table('entries', function(table) {
			table.dropColumn('board_id');
		})
	]);
};
