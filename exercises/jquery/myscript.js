// $('h1').click(function(){
//   console.log("Click!")
// })
//
// $('li').click(function(){
//   console.log("li click")
// })
// $('h1').click(function(){
//   $(this).text("I was changed with a click")
// })


// KEY PRESS

// $('input').eq(0).keypress(function(){
//   $('h3').toggleClass('turnBlue');
// })
// $('input').eq(0).keypress(function(event){
//   console.log(event);
// }) // it also worked with function(). Accented keys do not show up.


// On()

// $('h1').on('dblclick', function(){
//   $(this).toggleClass('turnBlue');
// })

// $('h1').on('mouseenter', function(){
//   $(this).toggleClass('turnBlue');
// })
// $('h1').on('mouseout', function(){
//   $(this).toggleClass('turnBlue');
// })


//ANIMATIONS
// $('input').eq(1).on('click', function(){
//   $('.container').fadeOut(3000) // all the content dissapears
// })
$('input').eq(1).on('click', function(){
  $('.container').slideUp(3000) // all the content dissapears
})
