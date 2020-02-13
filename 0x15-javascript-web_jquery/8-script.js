$(function () {
    $.ajax({
        type: 'GET',
        url: 'https://swapi.co/api/films/?format=json',
        success: function (data) {
            const results = data.results;
            for (let i = 0; i < results.length; i++) {
                console.log('success', data.results[i].title);
                $('ul#list_movies').append('<li>' + results[i].title + '</li>');
            }
        }
    });
});