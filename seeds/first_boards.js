'use strict';

exports.seed = function(knex, Promise) {
	return Promise.all([
		knex('boards').insert([
			{ name: 'politics', color: '93D74E' },
			{ name: 'music', color: 'FC5E00' },
			{ name: 'literature', color: 'FFDC1E' },
			{ name: 'tv', color: 'B70FD9' }
		])
	]);
};