// function myFunc (){
//     alert('halo')
// }
// var funcKu = ['makan', 10, false, myFunc, [4,5,['siapa',23, 'pentolan', [1, 2, 2, [312, 33, 12]]]]];
// console.log(funcKu[4][2][3][3][0])

// manipulasi array

// menambah array
// var myArr = []
// myArr[0] = 'siap'
// myArr[1] = 'iya'
// myArr[2] = 'oke'

// // mengurangi array

// var myArr = ['siap', 'kenapa', 'okey']
// myArr[2] = undefined

// // menampilkan seluruh isi array
// var myArr = [2,3,4,5,,6,7,8,9,10]
// console.log(myArr);

// // or
// for (var i = 0; i < myArr.length; i++){
//     console.log(myArr[i]);
// }

//  splice
// var arr = ['edric', 'galentino', 'nur', 'kenji', 'taryono']
// arr.splice(1,0,'jarel', 'candice', 'heaven');
// console.log(arr.join(' - '));

// slice
// var arr = ['edric', 'galentino', 'nur', 'kenji', 'taryono']
// var arr2 = arr.slice(0, 3)
// console.log(arr2.join(' - '));

// forEach

// var angka = [1,2,3,4,5,6,7,8]
// for (let i = 0; i < angka.length; i++) {
//     console.log(angka[i]);
// }
// angka.forEach(function (e) {
//     console.log(e);
// })
// var nama = ['edric', 'galentino', 'nur', 'kenji', 'taryono']
// nama.forEach(function(e, i) {
//     console.log('Mahasiswa ke ' + (i+1) + ' adalah ' + e);
// })

// map 

// var angka = [1,2,3,4,5,6,7,8]
// var angka2 = angka.map(function (p) {
//     return p
// })
// console.log(angka2);

// sort

// var angka = [1,2,3,4,5,6,7,8,5,6,7,3,6,4,5]
// var urutan = angka.sort()
// console.log(urutan);

// filter and find

// var angka = [1,2,3,4,5,6,7,8,5,6,7,3,6,4,5]
// var angka2 = angka.filter(function (p) {
//     return p == 3
// });
// console.log(angka2);














