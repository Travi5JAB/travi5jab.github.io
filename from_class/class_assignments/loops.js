for (let i = 1; i<= 20; i++){
    console.log(i)
}

console.log("");

for (let x = 1; x<=20; x++){
    console.log(x*3);
}

console.log("");

var numbers = [8, 2, 17, 4, 5, 10, 4, 8, 9, 15];

for(let i = 0; i < numbers.length; i++){
    console.log(numbers[i]*4);
}

console.log("");

for (let i = 1; i<= 20; i++){
    if( i % 2 === 0){
        console.log(i);
    }else{
        console.log("odd");
    }
}
console.log("");

for (let i = 10; i > 0; i--){
    console.log(i);
}

console.log("");


var letters = ["l", "e", "a", "r", "n"]
for (let i = 0; i<letters.length; i++){
    console.log(letters[i].toUpperCase());
}

console.log("");

var strings = ["hi", "yo", "there", "what", "how", "two", "are", "where", "you"]

for(let i = 0; i < strings.length; i++){
    if(i % 2 == 0){
        console.log(strings[i]);
    }
}

console.log("");


for (let i = 0; i<= 15; i++){
    if (i % 2 === 0){
        console.log("even");
    }else{
        console.log("odd");
    }
}
console.log("");


for (let i = 1; i <= 100; i++){
    if(i % 15 === 0){
        console.log("FizzBuzz");
    }else if (i % 3 === 0){
        console.log("Fizz");
    }else if (i % 5 === 0){
        console.log("Buzz");
    }else{
        console.log(i);
    }
}
