var first = prompt("What's your first name?");
var last = prompt("What's your last name?");
var age = prompt("How old are you?");
var height = prompt("How tall are you in cm?");
var pet = prompt("What's the name of your pet?");

alert("Thanks!")

if (first[0] == last[0] && age <30 && age > 20 && height >= 170 && pet[pet.length-1] === "y") {
  console.log("Hello spy.")
} else {
  console.log("Sorry, nothing to see here.");
}
