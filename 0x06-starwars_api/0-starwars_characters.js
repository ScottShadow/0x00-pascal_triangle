#!/usr/bin/node

const request = require('request');
movie_id = process.argv[2];

if (!movie_id || isNaN(movie_id) || process.argv.length < 3) {
  console.log('USE ./0-starwars_characters.js movie_id');
  process.exit(1);
}
// Define the URL
const url = `https://swapi-api.alx-tools.com/api/films/${movie_id}/`;

// Fetch JSON data
request({ url: url, json: true }, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  // Log the status code and response headers
  //console.log(`Status Code: ${response.statusCode}`);
  //console.log(`Response Headers: ${JSON.stringify(response.headers)}`);

  // Check if the response status code is 200 (OK)
  if (response.statusCode === 200) {
    // Log the parsed JSON data
    my_characters = body.characters;
    for (let i = 0; i < my_characters.length; i++) {
      request({ url: my_characters[i], json: true },
        (error, response, body) => {
          if (error) {
            console.error('Error:', error);
            return;
          }
          // Check if the response status code is 200 (OK)
          if (response.statusCode === 200) {
            // Log the parsed JSON data
            console.log(body.name);
          }
        })
    }
  } else {
    console.log(`Failed to retrieve data: ${response.statusCode}`);
  }
});
