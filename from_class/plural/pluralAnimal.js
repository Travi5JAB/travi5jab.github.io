var pluralAnimal = ["sheep", "geese", "children", "people", "fish","octopi"]
var animalname = ["sheep", "goose","child","person","fish","octopus"]


function pluralize(number,noun){
if(animalname.includes(noun) && number > 1){
    return number + " " + pluralAnimal[(animalname.indexOf(noun))];
}else if(pluralAnimal.includes(noun) && number === 1){
    return number + " " + animalname[(pluralAnimal.indexOf(noun))];
  }
    let wordArr = []
    for(let i = 0; i < noun.length; i++){
        let newArr = noun[i]
        wordArr.push(newArr[0])
      } var revWord = wordArr.reverse()
      if(revWord[0] === "s" && number === 1){
        revWord.shift()
        return number + " " + revWord.reverse().join("")
}
    let wordArr2 = []
    for(let i = 0; i < noun.length; i++){
        let newArr2 = noun[i]
        wordArr2.push(newArr2[0])
      } var revWord = wordArr2.reverse()
      if(revWord[0] === "s" && number > 1){
        return number + " " + revWord.reverse().join("")
}else if(number == 1 && noun.length>0){
  return number + " " + noun
}else if(number > 1 && noun.length>0){
    return number + " " + noun + "s";
}else if(number < 0){
  return "You Can't Have Negative Animals"
}else if(number === 0){
    return "How Many Animals Do You Want?"
}else{
    return "Enter number , Animal Name"
}

}
function buttonPress(){
var Text1 = document.getElementById("Text1").value; //number
var Text2 = document.getElementById("Text2").value;  //noun
    document.getElementById("answer").innerHTML = pluralize(parseInt(Text1), Text2);
}
