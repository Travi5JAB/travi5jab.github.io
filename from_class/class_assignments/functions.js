// function marco(){
//     return "Polo";
// }
//
// console.log(marco());
//
// console.log("");
//
// function greeting(name){
//     return "welcome " + name;
// }
//
// console.log(greeting("Travis"));
//
// console.log("");
//
// function oddOrEven(num){
//         if (num % 2 === 0){
//             return "even";
//         }else{
//             return "odd";
//         }
// }
//
// console.log(oddOrEven(3));
// console.log("");
//
// function triple(number){
//     return number *3
// }
// console.log(triple(7));
// console.log("");
//
// function multiply(num1, num2){
//     return num1 * num2;
// }
//
// console.log(multiply(5, 92));
// console.log("");
//
// function divisibleBy(n1,n2){
//     if (n1 % n2 === 0){
//         return n1 + " is divible by " + n2;
//     }else{
//         return "NOT Divisible"
//     }
// }
// console.log(divisibleBy(10,5));
// console.log(divisibleBy(10,6));
//
// function helloWorld(lang){
//     if(lang === "es"){
//         return "espanol";
//     }else if (lang === "de"){
//         return "Dutch?";
//     }else{
//         return "Hello World (English)";
//     }
// }
//
// console.log(helloWorld("es"));
// console.log(helloWorld("de"));
// console.log(helloWorld());
//
// function assignGrade(nScore){
//     if (nScore<=45){
//         return "F"
//     }else if (59>=nScore){
//         return "D"
//     }else if (79>=nScore){
//         return "C"
//     }else if (89>=nScore){
//         return "B"
//     }else{
//         return "A"
//     }
// }

//
// function assignGrade(nScore){
//     if (nScore >= 0){
//         return "A"
//     }else if(nScore <= 85){
//         return "B"
//     }
// }
// console.log(assignGrade(98));
// console.log(assignGrade(88));
// console.log(assignGrade(62));
// console.log(assignGrade(55));
// console.log(assignGrade(12));
// console.log("");



var pluralAnimal = ["sheep", "geese", "children", "people", "fish"]
var animalname = ["sheep", "goose","child","person","fish"]

//var noun = document.getElementById('Text2').value;

function pluralize(number, noun){

    if(animalname.includes(noun) && number > 1){
        return number + " " + pluralAnimal[(animalname.indexOf(noun))];
    }else if(pluralAnimal.includes(noun) && number == 1){
        return number + " " + animalname[(pluralAnimal.indexOf(noun))];
    }else if(number > 1){
        return number + " " + noun + "s";
    }else if(number == 1){
        return number + " " + noun;
    }else{
        return "Enter number , Animal Name"
    }

}
function buttonPress(){
var Text1 = document.getElementById("Text1").value;
var Text2 = document.getElementById("Text2").value;
    document.getElementById("answer").innerHTML = pluralize(Text1, Text2);
}
console.log(pluralize(1,"geese"));
console.log(pluralize(5,"child"));
console.log(pluralize(10,"dog"));
console.log(pluralize(3,"dogs")); // returns Dogss
console.log(pluralize(4,"person"));
