// membuat faktorial suatu bilangan
// ex: 5!=5x4x3x2x1
function factorial(e) {
    if (e == 0) return e = 1
    return e * factorial(e-1);
}
console.log(factorial(5));