var tanya = true
while (tanya) {
    
    //menangkap pilihan player
    var p = prompt('pilih: gajah, semut, orang')

    //menangkap pilihan computer
    //membangkitkan bilangan random
    var comp = Math.random()
    if (comp < 0.34) {
        comp = 'gajah'
    } else if (comp >= 0.34 && comp < 0.67) {
        comp = 'orang'
    } else {
        comp = 'semut'
    }
    //menentukan rules
    var hasil = ''
    if (p == comp) {
        hasil = 'SERI!'
    } else if (p == 'gajah') {
        // if (comp = 'orang') {
        //     hasil = 'MENANG!'
        // } else {
        //     hasil = 'KALAH!'
        // }
        hasil = (comp == 'orang') ? 'MENANG!' : 'KALAH!'
    } else if (p == 'orang') {
        hasil = (comp == 'semut') ? 'MENANG!' : 'KALAH!'
    } else if (p == 'semut') {
        hasil = (comp == 'gajah') ? 'MENANG!' : 'KALAH!'
    } else {
        hasil = 'memasukkan pilihan yang SALAH!'
    }
    //menampilkan hasil
    alert('Kamu memilih ' + p + ' dan computer memilih ' + comp + '\nMaka hasilnya : kamu ' + hasil)

    tanya = confirm('Lagi?')
}
alert('Terima kasih sudah bermain!')