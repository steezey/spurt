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
			table.string('provider_display');
			table.string('favicon_url', 510);
		}),
		knex.schema.createTable('entries', function(table) {
			table.increments();
			table.integer('item_id').unsigned().notNullable();
			table.integer('board_id').unsigned().notNullable();
			table.string('title', 510).notNullable();
			table.boolean('public').notNullable();
		}),
		knex.schema.createTable('boards', function(table) {
			table.increments();
			table.string('name').notNullable();
			table.string('color', 6).notNullable();
		}),
		knex.seed.run('first_boards')
	]);
};

exports.down = function(knex, Promise) {
	return Promise.all([
		knex.schema.dropTable('items'),
		knex.schema.dropTable('entries'),
		knex.schema.dropTable('boards')
	]);
};
