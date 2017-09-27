// Get the names of the players
var p1 = prompt('Name of player one?');
var p2 = prompt('Name of player two?');

// Toggle player names
$('h2').text(function(event){
  if ($(this).text() == ('Your play ' + p1)){
    $(this).text() = ('Your play ' + p2);
  } else {
    $(this).text('Your play ' + p1);
  }
})
