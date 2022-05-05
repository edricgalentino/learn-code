var chance = 2
var tanya = true
while (tanya) {
    //menangkap pilihan player
    var p = prompt('Pilih angka 1-10 \nKesempatanmu ada 3')
    //menangkap pilihan computer
    var comp = Math.random()
    if (comp <= 0.1) {
        comp = 1
    } else if (comp > 0.1 && comp <= 0.2) {
        comp = 2
    } else if (comp > 0.2 && comp <= 0.3) {
        comp = 3
    } else if (comp > 0.3 && comp <= 0.4) {
        comp = 4
    } else if (comp > 0.4 && comp <= 0.5) {
        comp = 5
    } else if (comp > 0.5 && comp <= 0.6) {
        comp = 6
    } else if (comp > 0.6 && comp <= 0.7) {
        comp = 7
    } else if (comp > 0.7 && comp <= 0.8) {
        comp = 8
    } else if (comp > 0.8 && comp <= 0.9) {
        comp = 9
    } else if (comp > 0.9 && comp <= 1) {
        comp = 10
    }
    //info tambahan
    var hasil = ''
    if (p == comp) {
        hasil = 'BENAR!'
    } else if (p < comp) {
        hasil = 'Terlalu rendah!'
    } else if (p > comp) {
        hasil = 'Terlalu tinggi!'
    }
    //hasil
    if (p == comp) {
        alert('Pilihan kamu ' + hasil)
        
    } else if (p < comp) {
        alert('Pilihan kamu ' + hasil + '\nKesempatanmu hanya tersisa ' + chance)
    } else {
        alert('Pilihan kamu ' + hasil + '\nKesempatanmu hanya tersisa ' + chance)
    }
    for (let chance = 2; chance >= 1; chance--){
        //menangkap pilihan player
        tanya = confirm('Pilih angka 1-10 \nKesempatanmu ada ' + chance)
    }
    
}
alert('Terima kasih sudah bermain!')
// var tanya = true
// while (tanya) {
    
//     //menangkap pilihan player
//     var p = prompt('pilih: gajah, semut, orang')

//     //menangkap pilihan computer
//     //membangkitkan bilangan random
//     var comp = Math.random()
//     if (comp < 0.34) {
//         comp = 'gajah'
//     } else if (comp >= 0.34 && comp < 0.67) {
//         comp = 'orang'
//     } else {
//         comp = 'semut'
//     }
//     //menentukan rules
//     var hasil = ''
//     if (p == comp) {
//         hasil = 'SERI!'
//     } else if (p == 'gajah') {
//         // if (comp = 'orang') {
//         //     hasil = 'MENANG!'
//         // } else {
//         //     hasil = 'KALAH!'
//         // }
//         hasil = (comp == 'orang') ? 'MENANG!' : 'KALAH!'
//     } else if (p == 'orang') {
//         hasil = (comp == 'semut') ? 'MENANG!' : 'KALAH!'
//     } else if (p == 'semut') {
//         hasil = (comp == 'gajah') ? 'MENANG!' : 'KALAH!'
//     } else {
//         hasil = 'memasukkan pilihan yang SALAH!'
//     }
//     //menampilkan hasil
//     alert('Kamu memilih ' + p + ' dan computer memilih ' + comp + '\nMaka hasilnya : kamu ' + hasil)

//     tanya = confirm('Lagi?')
// }
// alert('Terima kasih sudah bermain!')