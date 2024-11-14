#!/usr/bin/node

const request = require('request');

// Get movie ID from command line arguments
const movieId = process.argv[2];
const filmUrl = `https://swapi.dev/api/films/${movieId}/`;

// Function to get character name from URL
const getCharacterName = (url) => {
  return new Promise((resolve, reject) => {
    request(url, (error, response, body) => {
      if (error) {
        reject(error);
      } else {
        resolve(JSON.parse(body).name);
      }
    });
  });
};

// Main function to get and print characters
request(filmUrl, async (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    return;
  }

  const film = JSON.parse(body);
  const characterUrls = film.characters;

  try {
    // Get all character names and maintain order
    const characterPromises = characterUrls.map((url) => getCharacterName(url));
    const names = await Promise.all(characterPromises);

    // Print each name on a new line
    names.forEach((name) => console.log(name));
  } catch (err) {
    console.error('Error fetching characters:', err);
  }
});
