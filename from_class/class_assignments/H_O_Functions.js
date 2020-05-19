// multiply array info by 10 and return new array
var arr1 = [3, 9, 15, 4, 10]
mult10 = (array) =>{
  let newArr = array.map(value => value * 10)
        return newArr
      }
console.log(mult10(arr1));
// outputs -> [30, 90, 150, 40, 100]
console.log("");
/////////////////////////////////////////////////////////////////////////////

// Write an anonymous function that takes in an array and returns a new array with only odd numbers
var arr2 = [2, 7, 3, 5, 8, 10, 13]
odds =(array) => array.filter(number => number % 2);

console.log(odds(arr2));
// expected output = [7, 3, 5, 13]
console.log("");
//////////////////////////////////////////////////////////////////////////

// Write a function that takes in an array of numbers and letters and returns a
// new array with only the letters. HINT: use typeof() method.

var combo_arr = [7, "n", "i", "c", 10, "e", "w", 3, "o", "r", "k"]
stringOnly = (arr) =>{
    return newArr= arr.filter(value => typeof value === "string")
}
console.log(stringOnly(combo_arr));
console.log("");
///////////////////////////////////////////////////////////


var animals = [
  { name: "Waffles", type: "dog", age: 12 },
  { name: "Fluffy", type: "cat", age: 14 },
  { name: "Spelunky", type: "dog", age: 4 },
  { name: "Hank", type: "cat", age: 11 },
];

catsOnly = (arr) => {
    var {name,type,age} = arr
    return newArr= arr.filter(value => value.type === "cat")
}
console.log(catsOnly(animals))
console.log("");

nameOnly = (arr) => {
    var {name, type, age} = arr
    return newArr= arr.map(value => value.name)
}
console.log(nameOnly(animals));
console.log("");
/////////////////////////////////////////////////////////////

// Create a function that takes in a string and
// returns a new string with all the vowels removed.

var str = "javascript is awesome"
// expected output -> "jvscrpt s wsm"
// console.log(str.split(""));

noVowel = (string) => {
    var vowel = ["a","e","i","o","u"]
    var split = string.split("")
    return newArr = split.filter(value =>{ return !vowel.includes(value)})


}
console.log(noVowel(str));
console.log("");
///////////////////////////////////////////////////////////////////

// Create a function that merges two arrays, takes in two arrays as arguments returns one array with no duplicate values.

var arr1 = [3, 7, 10, 5, 4, 3]
var arr2 = [7, 8, 2, 1, 5, 4]

noDups = (array1,array2) => {
    var ccArr = array1.concat(array2)
    // console.log(ccArr);
    return ccArr.filter((value,index) => ccArr.indexOf(value)===index)

    }

// expected output -> [3, 7, 10, 5, 4, 8, 2, 1]
console.log(noDups(arr1,arr2));
