// contoh perhitungan matematika tanpa function

// var a = 7
// var b = 4
// var volumeA
// var volumeB
// var total

// volumeA = a * a * a
// volumeB = b * b * b

// total = volumeA + volumeB
// console.log(total);

// before refactoring
// function jumlahVolumeDuaKubus(a, b) {
//     volumeA = a * a * a
//     volumeB = b * b * b

//     total = volumeA + volumeB
//     return total
// }
// alert(jumlahVolumeDuaKubus(7, 4))
// alert(jumlahVolumeDuaKubus(8, 6))
// alert(jumlahVolumeDuaKubus(9, 13))

// after refactoring (lebih efisien)

function jumlahVolumeDuaKubus(a, b) {
    return a * a * a + b * b * b
}
alert(jumlahVolumeDuaKubus(7, 4))
alert(jumlahVolumeDuaKubus(8, 6))
alert(jumlahVolumeDuaKubus(9, 13))