// Intro to Javascript Assessments

// Consider this variable:

var mantra = "Be the dev";

// 1. Write the code that returns 'B' from mantra.
console.log(mantra.charAt(0))
// 2. Write the code that determines if there is a 'x' in mantra.
console.log(mantra.includes("x"));
// 3. Write the code that determines if there is a 'v' in mantra.
console.log(mantra.includes("v"));
// Stretch: Write the code that returns the position of 'v' in mantra.
console.log(mantra.indexOf("v"));

// Consider the following statement:

var codingIsEasy = true
var imBored = true

if (codingIsEasy && imBored) {
    console.log("I need more!")
} else {
    console.log("Steady as she goes")
}

// 4. Update the codingIsEasy and imBored variables above the statement to the values required to log "I need more!"

// Consider the following statement:

var imLost = false
var imFrustrated = false

if (imLost || imFrustrated) {
    console.log('Break time!')
} else {
    console.log('Keep coding!')
}

// 5. Update the imLost and imFrustated variables above the statement to the values required to log "Keep coding!"

// 6a. Recall the mantra variable from the first question. Write the code that logs each letter of mantra using a for loop.
for (let i = 0; i< mantra.length; i++){

  console.log(mantra[i])
}
console.log("");
// Stretch: Using a while loop.
let ind = 0
while( ind< mantra.length ){
  console.log(mantra[ind])
  ind++
}
// Super Stretch: Using forEach().

// Consider the following variable:
console.log("");
var message = "thisisateststring"
var number = 55
var boolean = true
// 7. Write a function that takes a string like message as an argument and returns the string without vowels.
var vowel = ["a","e","i","o","u"]
var newStr = message.split()
function remVowel(string){
    var newArr = []
    if (typeof string != "string"){
      return "ERROR: This is a "+typeof string+ " not a string"
    }else{
        for(i=0; i<string.length; i++){
            if(string[i]!= "a" && string[i]!= "e" && string[i]!= "i" && string[i]!= "o" && string[i]!= "u"){
                newArr.push(string[i])
                var x = newArr.join("")
              }

        }return x
      }
}
console.log(remVowel(message));
console.log(remVowel(number));
console.log(remVowel(boolean));
console.log("");
// Stretch: Update your function to throw an exception if the argument is not a string.

// Super Duper Stretch: Update your function to throw a TypeError if the argument is not a string.

// Consider the following variable:

var toonimals = [ {name: 'Itchy', animal: 'mouse'}, {name: 'Stimpy', animal: 'cat'}, {name: 'Daffy', animal: 'duck'}, {name: 'Scratchy', animal: 'cat'}, {name: 'Ren', animal: 'dog'}, {name: 'Felix', animal: 'cat'}]

// 8. Write a function that takes an array like toonimals and returns an array with only the toons that are cats.

function cats(arr){
//make for loop and use obj.animal
var newArr =[]
  for(var i = 0; i< arr.length; i++){
     if(arr[i].animal === "cat" ){
       newArr.push(arr[i])


     }
  }return newArr
}


console.log(cats(toonimals));
