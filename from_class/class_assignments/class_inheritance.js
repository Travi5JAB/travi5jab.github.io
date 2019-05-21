class Car{
    constructor(speed=0){
        this.model = "car"
        this.wheels = 4
        this.modelYear = 1992
        this.lights = "OFF"
        this.signal = "OFF"
        this. speed = speed
    }
    lightsTog(){
        if(this.lights==="OFF"){
            this.lights = "ON"
            return this.lights
        }else{
            this.lights = "OFF"
            return this.lights
    }
}
    sigRight(){
        this.signal = "right"
        return this.signal
        // this.signal = "OFF"
    }
    sigLeft(){
        this.signal = "left"
        return this.signal
        // this.signal = "OFF"
    }
    accelerate(speedUP){
        this.speed =  this.speed + speedUP
        return this.speed
    }
    break(speedDown){
        this.speed = this.speed - speedDown
        return this.speed
    }
}
class Tesla extends Car{
    constructor(speed){
        super(speed)
        this.modelYear = 2019
        this.model = "Tesla"
    }
}
class Tata extends Car{
    constructor(speed){
        super(speed)
        this.modelYear = 1984
        this.model = "Tata"
    }
}
class Toyota extends Car{
    constructor(speed){
        super(speed)
        this.modelYear = 2000
        this.model = "Toyota"
    }
}
class Tesla2 extends Car{
        constructor(speed){
            super(speed)
            this.modelYear = 2017
            this.model = "Tesla"
        }
    }
class Tata2 extends Car{
        constructor(speed){
            super(speed)
            this.modelYear = 1974
            this.model = "Tata"
        }
    }
class Toyota2 extends Car{
        constructor(speed){
            super(speed)
            this.modelYear = 1980
            this.model = "Toyota"
        }
}

var myCar = new Car()
var myTesla = new Tesla()
var myToyota = new Toyota()
var myTata = new Tata()
var myTesla2 = new Tesla2()
var myToyota2 = new Toyota2()
var myTata2 = new Tata2()

var myGarage = [myTesla,myToyota,myTata,myTesla2,myToyota2,myTata2]

yoC = (arr) => {
var {wheels, modelYear, lights, signal, speed} = arr
return newArr= arr.map(value => value.modelYear)
}

moC = (arr) => {
var {wheels, modelYear, lights, signal, speed} = arr
return newArr= arr.map(value => value.model)
}


console.log(moC(myGarage),yoC(myGarage));
// console.log(myGarage);
// myTesla.accelerate(10)
// myTesla.break(7)
// myTata.accelerate(2)
// myTata.break(1.25)
// myToyota.accelerate(7)
// myToyota.break(5)
// console.log(myToyota.modelYear);
// myTesla.sigLeft()
// myTesla.lightsTog()
// console.log(myCar);
// console.log(myTesla);
// console.log(myToyota);
// console.log(myTata);
// console.log(myTesla.lightsOn())
// console.log(myTesla.lightsOff())
// console.log(myTesla.sigLeft());


///// do next!!!!!!!! speed  of car
