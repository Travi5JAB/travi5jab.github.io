console.log("Script Called");
var answers = ["Yup!", "Fuhgeddaboudit", "Maybe", "What would your mother do?","What would an Australian do, then do the opposite"," Your answer here"]

function ball(){
    var i = answers.length
    var random = Math.floor(Math.random()*i)
    var question = document.getElementById("textbox").value
    document.getElementById("questioninput").innerHTML = question + "?"
    if(question.length>0){
      document.getElementById("answer").innerHTML = answers[random];
    }else{
      document.getElementById("answer").innerHTML = "TRY AGAIN LATER"
    }
}

// animation shake ball

element = document.getElementById("eightballDiv");

element.addEventListener("click", function(e) {
  e.preventDefault;
  element.classList.remove("shakeball");

  element.offsetWidth = element.offsetWidth;

  element.classList.add("shakeball");
}, false);

// animation turn triangle

element = document.getElementById("triangle");

element.addEventListener("click", function(e) {
  e.preventDefault;
  element.classList.remove("turntriangle");

  element.offsetWidth = element.offsetWidth;

  element.classList.add("turntriangle");
}, false);

function myFunction() {
  var x = document.getElementById("answer");
  if (x.style.display === "none") {
    x.style.display = "block";
  }
}
