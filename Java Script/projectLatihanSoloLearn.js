// (liat di sololearn untuk lebih lengkapnya)
// 1 travel 
// function main() {
//     var distance = parseInt(readLine(), 10);
//     // my code goes here
//     let average = 40
//     let anHour = 60
//     let averageHour = distance/average
//     let minutes = averageHour*anHour
//     console.log(minutes);
// }
// 2 snail 

// function main() {
//     var depth = parseInt(readLine(), 10);
//     //your code goes here
//     let climb = 7
//     let slipBack = 2
//     let day = 0
//     for (workDone = 0; workDone <= depth;) {
//         day += 1;
//         workDone += climb
//         if (workDone >= depth){
//             break;
//         }
//         workDone -= slipBack;
//     }
//     console.log(day)
// }

// 3. currency converter

// function main() {
//     var amount = parseFloat(readLine(), 10);
//     var rate = parseFloat(readLine(), 10);
    
//     console.log(convert(amount, rate));
// }
// function convert(amount, rate){
//     let total = amount*rate
//     return total
// }

// 4. contact manager

// function contact(name, number) {
//     this.name = name;
//     this.number = number;
//     this.print = print;
// }
// function print(){
//     console.log(this.name + ': ' + this.number) 
// }

// var a = new contact("David", 12345);
// var b = new contact("Amy", 987654321);


// a.print();
// b.print();

// 5 store manager

// function main() {
//     var increase = parseInt(readLine(), 10);
//     var prices = [98.99, 15.2, 20, 1026];
//     //your code goes here
//     for (i=0; i<prices.length; i++){
//         prices[i] += increase
//     }
    
//     console.log(prices)
// }
