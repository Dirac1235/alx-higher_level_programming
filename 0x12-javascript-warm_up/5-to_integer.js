#!/usr/bin/node
const { argv } = require('node:process');
let val = parseInt(argv[2])

if ( isNaN(val)) {
	console.log('Not a number');
} else {
	console.log('My number: ' + val);
}
