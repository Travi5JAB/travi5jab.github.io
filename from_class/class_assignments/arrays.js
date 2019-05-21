var groceryList2 = ["chips", "dip", "cookies"]
console.log(groceryList2.push("soda"));
console.log(groceryList2)


var numbers2 = [2, 4, 6, 8, 10];
numbers2.unshift(0)
console.log(numbers2)


var groceryList1 = ["apples", "carrots", "oatmeal"]
var additem =["granola"]
var cc = groceryList1.concat(additem)
console.log(cc);
console.log(groceryList1);

var numbers1 = [1, 2, 3, 4, 5]
var zero = [0]
console.log(zero.concat(numbers1));

var numbers3 = [2, 13, 6, 8, 4, 2]
console.log(numbers3.indexOf(2));


var chars = ["y", "a", "r", "r", "a"]
var join = chars.join("")
var charsReversed = chars.reverse("")
var joinedRev = charsReversed.join("-")
console.log(join);
console.log(joinedRev);

var sibling =["jim", "frankie", "kaja", "weezer"]
var parents = ["laurie", "janet", "diane", "gaetano"]
var ss = sibling.sort()
console.log(ss);
var ps = parents.sort()
var pr = ps.reverse("")
console.log(pr);
var fullList = sibling.concat(parents)
var fullSorted =fullList.sort()
var rfS = fullSorted.reverse()
console.log(rfS);
