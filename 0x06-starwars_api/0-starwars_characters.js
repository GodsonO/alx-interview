#!/usr/bin/node

const httprequest = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${movieId}`;

httprequest(url, async (err, res, body) => {
  err && console.log(err);

  const charactersArr = (JSON.parse(res.body).characters);
  for (const character of charactersArr) {
    await new Promise((resolve, reject) => {
      httprequest(character, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
