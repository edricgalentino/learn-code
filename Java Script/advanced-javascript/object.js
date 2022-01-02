let score = prompt('Masukkan NPM anda : ')
let mystery = 0;

for (const chara in score) {
    if (chara == 9) {
        break
    } if (chara % 2 > 0) {
        continue
    } else {
        mystery += chara
    }
    console.log(mystery);
}