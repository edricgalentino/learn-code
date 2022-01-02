var s = ''
var space = ' '
for (let p = 0; p < 10; p++) {
    space += ' .'
}
for (let i = 1; i <= 10; i++) {
    for (let j = 0; j < i; j++) {
        s += '*'
    }
    s += '\n'
}


console.log(s);