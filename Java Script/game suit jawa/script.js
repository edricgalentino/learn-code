function getPilihanComputer() {
    const comp = Math.random();
    if (comp < 0.34) return 'gajah';
    if (comp >= 0.34 && comp < 0.67) return 'orang';
    return 'semut';
};

function getHasil(comp, player) {
    if (player == comp) return 'SERI!';
    if (player == 'gajah')
        return (comp == 'orang') ? 'MENANG!' : 'KALAH!';
    if (player == 'orang')
        return (comp == 'semut') ? 'MENANG!' : 'KALAH!';
    if (player == 'semut')
        return (comp == 'gajah') ? 'MENANG!' : 'KALAH!';
};

function putar() {
    const imgComputer = document.querySelector('.img-komputer');
    const gambar = ['gajah', 'semut', 'orang']
    let i = 0;
    const waktuMulai = new Date().getTime();
    setInterval(() => {
        if (new Date().getTime() - waktuMulai > 1000) {
            return;
        };
        imgComputer.setAttribute('src', 'img/' + gambar[i++] + '.png')
        if (i > 2) i = 0;
    }, 100);
}

function score(hasil) {
const score = document.querySelector('.score');
let i = 0;
let j = 0;
if (hasil === "MENANG!") {
    return score.innerHTML = i++ + ' - ' + j
    }
    if (hasil === "KALAH!") {
        return score.innerHTML = i + ' - ' + j++
    }
    // if (hasil === "MENANG!") {
    //     for (let i = 0; i <= 5; i++) {
    //         return score.innerHTML = i + ' - ' + j
    //     }
    // }
    // if (hasil === "KALAH!") {
    //     for (let j = 0; j <= 5; j++) {
    //         return score.innerHTML = i + ' - ' + j
    //     }
    // }
}

const pilihan = document.querySelectorAll('li img');
pilihan.forEach(function (p) {
    p.addEventListener('click', function () {
        const pilihanComputer = getPilihanComputer();
        const pilihanPlayer = p.className;
        const hasil = getHasil(pilihanComputer, pilihanPlayer);
        const info = document.querySelector('.info');
        const imgComputer = document.querySelector('.img-komputer');
        putar();
        setTimeout(() => {
            imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
            info.innerHTML = hasil;            
        }, 1000);
        info.innerHTML = '';
        score(hasil);
    })
})

















// const gajah = document.querySelector('.gajah');
// const orang = document.querySelector('.orang');
// const semut = document.querySelector('.semut');

// gajah.addEventListener('click', function () {
//     const pilihanComputer = getPilihanComputer();
//     const pilihanPlayer = gajah.className;
//     const hasil = getHasil(pilihanComputer, pilihanPlayer);
//     const info = document.querySelector('.info');
//     const imgComputer = document.querySelector('.img-komputer');
//     imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
//     info.innerHTML = hasil;
// });
// orang.addEventListener('click', function () {
//     const pilihanComputer = getPilihanComputer();
//     const pilihanPlayer = orang.className;
//     const hasil = getHasil(pilihanComputer, pilihanPlayer);
//     const info = document.querySelector('.info');
//     const imgComputer = document.querySelector('.img-komputer');
//     imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
//     info.innerHTML = hasil;
// });
// semut.addEventListener('click', function () {
//     const pilihanComputer = getPilihanComputer();
//     const pilihanPlayer = semut.className;
//     const hasil = getHasil(pilihanComputer, pilihanPlayer);
//     const info = document.querySelector('.info');
//     const imgComputer = document.querySelector('.img-komputer');
//     imgComputer.setAttribute('src', 'img/' + pilihanComputer + '.png');
//     info.innerHTML = hasil;
// });

