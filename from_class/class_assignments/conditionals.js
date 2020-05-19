var item =200

if (item < 100){
    console.log("in budget");
}

console.log("");

var hungry = true
if (hungry === true){
    console.log("eat food");
}else{
    console.log("keep coding");
}

console.log("");

var trafficLight = "green"
if (trafficLight === "green") {
    console.log("Go");
} else if (trafficLight === "yellow") {
    console.log("Slow down");
} else if (trafficLight === "red") {
    console.log("Stop");
} else {
    console.log("error");
}

console.log("");

var num1 = 10
var num2 = 10

if (num1 > num2){
    console.log(num1);
}else if(num2 > num1){
    console.log(num2);
}else if (num1 === num2){
    console.log("equal");
}else{
    console.log("input a number");
}

console.log("");

var num = 8
if(num  === 0){
    console.log("Number is 0");
}else if(num % 2 === 1){
    console.log("odd");
}else if (num % 2=== 0){
    console.log("Even");
}

console.log("");

var grade = 72
if (grade === 100) {
    console.log("perfect score");
} else if (grade === 0) {
    console.log("no grade available");
} else if (grade<=99 && grade>=81){
    console.log("A");
}else if (grade<=80 && grade>=70){
    console.log("B");
}
// etc...

else{
    console.log(grade+"%");
}

console.log("");

var a = true
if ((typeof(a)) === "string"){
    console.log("String");
}else if ((typeof(a)) === "number"){
    console.log("Number");
}else if ((typeof(a)) === "boolean"){
    console.log("Boolean");
}else {
    console.log("ERROR");
}

console.log("");
