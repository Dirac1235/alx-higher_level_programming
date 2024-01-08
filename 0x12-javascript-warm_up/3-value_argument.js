#!/usr/bin/node
const { argv } = require('node:process');
let count = 0;
for (let x in argv) {
	count = count + 1
	if (count === 3) {
		console.log(argv[2]);
		break;
	}
}
if (count != 3) {
	console.log('No argument');
}