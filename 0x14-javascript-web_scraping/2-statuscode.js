#!/usr/bin/node
const url = 'https://alx-intranet.hbtn.io/status';

fetch(url)
  .then(response => response.text()) // Get the response body as text
  .then(data => console.log(data)) // Print the response data (status code)
  .catch(error => console.error(error)); // Handle errors

