
// Restart game button
var restart = document.querySelector("#b")

// Grabs all squares
var squares = document.querySelectorAll("td")
// Clear all squares
function clearBoard(){
  for (var i = 0; i < squares.length; i++){
    squares[i].textContent = "";
  }
}

// Check the square marker
function changeMarker(){
  if(this.textContent === ""){
    this.textContent = "X";
  }else if (this.textContent === "X"){
  this.textContent = "0";
}else {this.textContent = ""; }
}
for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener("click", changeMarker)
}

restart.addEventListener("click", clearBoard)
// For loop to add event listeners to all squares
