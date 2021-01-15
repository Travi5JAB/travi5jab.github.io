// <!-- apps rotation functions on portfolio page-->

// apps in apps folder
var urls = [
  'apps/cloudCulture.html',
  'apps/colissionTech.html',
  'apps/diceRoll.html',
  'apps/eightBall.html',
  'apps/highLow.html',
  'apps/kingspireMedia.html',
  'apps/joelsClinic.html',
  'apps/pigLatin.html',
  'apps/pluralizer.html',
  'apps/skillTree.html',
  'apps/yourPayrollMan.html'
];

// change image every so often
// use if to check if # is the same !!!!!!!!
var randTimer = setInterval(function() {
  var randTime = Math.floor(Math.random()*urls.length);
  if(randTime == oldNum && randTime !== urls.length - 1){
    randTime = randTime + 1
    var oldNum = randTime
  }else if (randTime == oldNum){
    randTime = 0
    var oldNum = randTime
  }
  document.getElementById('myiframe').src = urls[randTime];
}, 15000);


// set random image
var rand = Math.floor(Math.random()*urls.length);
// go back in array
function back(){
  if(rand === 0 ){
    // shift to end if at beggining of array
    var element = document.getElementById('myiframe')
    element.classList.add("animateLeft");
    var timer = setInterval(function() {
      element.classList.remove("animateLeft");
      clearInterval(timer);
    }, 1000);
    var timer2 = setInterval(function() {
      element.src = urls[urls.length - 1];
      rand = urls.length - 1
      clearInterval(timer2);
    }, 500);
  }else{
    var element = document.getElementById('myiframe')
    element.classList.add("animateLeft");
    var timer = setInterval(function() {
      element.classList.remove("animateLeft");
      clearInterval(timer);
    }, 1000);
    var timer2 = setInterval(function() {
      element.src = urls[rand - 1];
      rand = rand - 1
      clearInterval(timer2);
    }, 500);
  }
}

// go fwd in array
function forward(){
  if(rand === urls.length - 1 ){
    // shift to beginning if at end of array
    var element = document.getElementById('myiframe')
    element.classList.add("animateRight");

    // remove animation
    var timer = setInterval(function() {
      element.classList.remove("animateRight");
      clearInterval(timer);
    }, 1000);

    // change image halfway
    var timer2 = setInterval(function() {
      element.src = urls[0];
      rand = 0
      clearInterval(timer2);
    }, 500);
  }else{
    var element = document.getElementById('myiframe')
    element.classList.add("animateRight");

    // remove animation
    var timer = setInterval(function() {
      element.classList.remove("animateRight");
      clearInterval(timer);
    }, 1000);

    // change image halfway
    var timer2 = setInterval(function() {
      element.src = urls[rand + 1];
      rand = rand + 1
      clearInterval(timer2);
    }, 500);
  }
}
