#!/usr/bin/node
//Get Character from swapi.dev (but holberton)

const url = 'https://swapi-api.hbtn.io/api/people/5/?format=json';

$.get(url, function (data, textStatus) {
    $('div#character').text(data.name);
});
