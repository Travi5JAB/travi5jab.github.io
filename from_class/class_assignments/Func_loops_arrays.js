var arr1 = [3, 9, 15, 4, 10]

function timesThree(arr){
    var newArr = []
    for(let i = 0; i <arr.length; i++){
    newArr.push(arr[i]*3)

    }
    return newArr
}
console.log(timesThree(arr1));

var arr2 = [2, 7, 3, 5, 8, 10, 13]
function oddNum(arr) {
    newArr = []
    for(i = 0; i < arr.length; i++) {
        if (arr[i]%2 != 0) {
            newArr.push(arr[i])
        }
    } return newArr
}
console.log(oddNum(arr2));


var sent = "Hello There"

function allCap(string){
    var newString = string.toUpperCase()
    return newString
}
console.log(allCap(sent));

var combo_arr = [7, "n", "i", "c", 10, "e", "w", 3, "o", "r", "k"]
function letters(arr) {
    newArr = []
     for(i = 0; i < arr.length; i++) {
         if (typeof(arr[i])==="string") {
             newArr.push(arr[i])
         }
     }return newArr
}
console.log(letters(combo_arr));


var highestNumber = [1,4,2,7,15,2,77,5]
function nums(arr){
    var max = 0
    for (i = 0; i  < arr.length; i++){
        if(arr[i]> max){
            max = arr[i]
        }
    }return max
}console.log(nums(highestNumber));

var Number = [1,4,2,7,15,2,77,5]
function nums(arr){
    var lowest = 1
    for (i = 0; i  < arr.length; i++){
        if(arr[i]< lowest){
            lowest = arr[i]
        }
    }return lowest
}console.log(nums(Number));


var nums = [1,2,3]
function sum1(arr){
    var newNum = 0
    for(i = 0; i < arr.length; i++){
            newNum = arr[i]+newNum
            // console.log(newNum);
    }return newNum
}

console.log(sum1(nums));



var nums = [1,2,3]
function sum1(arr){
    var newNum = 0
    var mean = 0
    for(i = 0; i < arr.length; i++){
            newNum = arr[i]+newNum
            mean = newNum/arr.length
            // console.log(newNum);
    }return mean
}

console.log(sum1(nums));

var highestNumber = [1,4,2,7,15,2,77,5]
function nums(arr){
    var max = 0
    var ind = 0
    for (i = 0; i  < arr.length; i++){
        if(arr[i]> max){
            max = arr[i]
            ind = arr.indexOf(max)
        }
    }return ind
}console.log(nums(highestNumber));
var blank = [2,7]
function fillArray(arr){
    var newArr = []
    var insNum = arr[1]
    for (i = 0; i  < arr[0]; i++){
            newArr.push(insNum)
    }return newArr
}console.log(fillArray(blank));

var filterA = [58, '', 'abcd', true, null, false, 0]
function filt(arr){
    newArr = []
    for (i = 0; i  < arr.length; i++) {
        if (arr[i]!= null && arr[i]!= false && arr[i]!= 0 && arr[i]!= "") {
            newArr.push(arr[i])
        }
    }return newArr
}
console.log(filt(filterA));

var random = Math.floor(Math.random()*100+1)
function guess(number){
    if (number > random){
        return "Too High"
    }else if (number < random){
        return "Too Low"
    }else if (number === random){
        return random + "! you got it"
    }else{
        return "ERROR!!!!"
    }
}
console.log(random);
console.log(guess(100));
console.log(guess(75));
console.log(guess(50));
console.log(guess(25));
console.log(guess(0));
console.log(guess("e"));


var str1= "damon nomad"
// var new1 = ""
function reverseString(str) {
    var new1 = str.split("").reverse().join("");
        if (new1===str){
             return "yes "+ str+ "  is a palindrome."
        }else{
            return "NO "+ str+ " is not a palindrome"
        }
}
console.log(reverseString(str1));


var strings = "javascript is awesome"
var vowel = ["a","e","i","o","u"]
var newStr = strings.split()
function remVowel(string){
    var newArr = []
    for(i=0; i<string.length; i++){
        if (string[i]!= "a" && string[i]!= "e" && string[i]!= "i" && string[i]!= "o" && string[i]!= "u") {
                newArr.push(string[i])
                var x = newArr.join("")
            }
        }return x
}
console.log(remVowel(strings));
newArr = [3, 7, 10, 5, 4, 3, 7, 8, 2, 1, 5, 4]

var arr1 = [3, 7, 10, 5, 4, 3]
var arr2 = [7, 8, 2, 1, 5, 4]


function mergeNoDup(arrA, arrB){
    var newArr = arrA.concat(arrB)
    var empty = []
    for( i = 0; i < newArr.length; i++){
        if( empty.includes(newArr[i])===false){
             empty.push(newArr[i])

        }
    }
    return empty
}
console.log(mergeNoDup(arr1,arr2));
