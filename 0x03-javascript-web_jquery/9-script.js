#!/usr/bin/node
// fetch Hello, from the headtag

const url = 'https://stefanbohacek.com/hellosalut/?lang=fr';

window.onload = function() {
    $.getJSON(url, function(data, status) {
        $('DIV#hello').text(data.hello);
    });
};

