// // Get the names of the players
// // var p1 = prompt('Name of player one? ');
// // var p2 = prompt('Name of player two?');
//
// // Toggle player names
// // $('h2').text(function(event){
// //   if ($(this).text() == ('Your play ' + p1)){
// //     $(this).text() = ('Your play ' + p2);
// //   } else {
// //     $(this).text('Your play ' + p1);
// //   }
// // })


// Logic for changing colors of buttons
// Based on row click, turn blue or red if grey

// Capture click on row
$('tr').on('click', function(){
  // Get column buttons
  var buttons = $(this).find('button');
  console.log(buttons);
  // Get last empty button
  // for (b of buttons){
  //   if ($(b).css('background-color') == 'grey'){
  //     console.log("hello");
  //   }
  // }
})
