$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  for (i in data.results) {
    $('UL#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
