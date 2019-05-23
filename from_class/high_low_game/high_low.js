console.log("connected");
var random = Math.floor(Math.random()*100+1)
// make counter decrease by one inside guess

function guess(number){
    if (number > random){
        return "Your Number is: Too High"
    }else if (number < random){
        return "Your Number is: Too Low"
    }else if (number == random){// 3 = will pass this in html???? not sure why
      alert("You Win")
      document.location.reload();
      clearInterval(interval)
    }else{
        return "ERROR!!!!"
    }
}
var lives = 7;
function loseLife() {
    lives -= 1;
    if (lives < 0) {
        lives = 0;
    }if(lives === 0){
      alert("You Lose")
      document.location.reload();
      clearInterval(interval)
    }
    document.getElementById("life").innerHTML = "Lives Left: "+lives;
}


function buttonPress(){
    var Text1 = document.getElementById("Text1").value;
        document.getElementById("answer").innerHTML = guess(Text1);
}
console.log(random);

// console.log(guess(100));
// console.log(guess(75));
// console.log(guess(50));
// console.log(guess(25));
// console.log(guess(0));
// console.log(guess("e"));
