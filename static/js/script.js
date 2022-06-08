var speed = document.getElementById("speed");
var output = document.getElementById("valueSpeed");

output.innerHTML = speed.value; 

speed.oninput = function() {
  output.innerHTML = this.value;
}