#!/usr/bin/node

const request = require('request');
const star_wars_uri = 'https://swapi-api.hbtn.io/api/films/'.concat(process.argv[2]);

request(star_wars_uri, function (_err, _res, body) {
  body = JSON.parse(body);
  console.log(body.title);
});
