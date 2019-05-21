const oldEnough = (name,age) => (age >= 21) ? name + " is " +age+ ", so they can drink" : name + " is " +age+", so they can NOT drink"


console.log(oldEnough("john",55))
console.log(oldEnough("jim",5))
console.log(oldEnough("tom",21))
console.log(oldEnough("amy",27))
console.log("");
//////////////////////////////////////////////////////////////////////////////

var greaterNum = (num1,num2) => (num1 > num2) ? num1 + " is greater than " +num2 : num1 + " is less than " +num2

console.log(greaterNum(5,7));
console.log(greaterNum(7,4));
console.log(greaterNum(51,2));
console.log("");
///////////////////////////////////////////////////////////////////////////

var person = {
  name: "Alex Keaton",
  phone: 123456789,
  getData() { return this.name+"-"+this.phone }
};

var {name, phone} = person
console.log(name);
console.log(phone);
console.log("");
//////////////////////////////////////////////////////////////////////

var sentence = (...words) =>  words.join(" ")
var ex1 = "you can"
var ex2 = "also"
var ex3 = "use variables"

console.log(sentence("this", "function", "works", "and", "joins", "multiple", "strings","..."))
console.log(sentence(ex1,ex2,ex3))
console.log("");
////////////////////////////////////////////////////////////////////////
var customer = { name: "Foo" }
var card = { amount: 7, product: "Bar", unitprice: 42 }
var {amount,product,unitprice} = card

var message = `Hello ${customer.name},
want to buy ${card.amount} ${card.product} for
a total of ${card.amount * card.unitprice} bucks?`
console.log(message);
console.log(amount);
console.log("");

// Can you come up with a function that uses all 3 of these?
// Arrow Functions
// String Interpolation
// Object Destructuring
var person1={name: "Sam",age: 17}
var person2={name: "Sam",age: 21}
var person3={name: "Sam",age: 45}

// var {name,age} = people
var oldEnough = (people={name,age}) => (people.age >= 21) ? `${people.name} is ${people.age} so they can drink` : `${people.name} is ${people.age} so they can NOT drink`

// console.log(oldEnough(name,age));
console.log(oldEnough(person1));
console.log(oldEnough(person2));
console.log(oldEnough(person3));
