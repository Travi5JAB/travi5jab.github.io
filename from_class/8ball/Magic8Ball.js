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
