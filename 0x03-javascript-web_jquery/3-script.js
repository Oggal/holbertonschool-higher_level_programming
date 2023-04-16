#!/usr/bin/node
//Update class of <header> tag to red, using JQUERY


$('div#red_header').click(
    function() {
        $('header').addClass('red');
    }
);
