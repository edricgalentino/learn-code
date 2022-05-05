var f;
f = 45;
console.log('hello world')
console.log('isi dari f adalah ' + f)

// gabisa langung open in browser, karena emang harus pake HTML biar bisa. File ada di folder CSS>u.html
alert('Mulai');
for( var i = 0; i < 5; i++){
    alert('Hello World!');
}
alert('Selesai');

// function declaration & function ekspression
// function declaration
function pesanAwal(nama){
    alert("Halo " + nama)
}
pesanAwal('Edric')

// function ekspression 
var sapaan = function (nama) {
    alert('Halo ' + nama)
}
sapaan('Galentino')

// array
var funcKu = ['makan', 10, false, myFunc, [4,5,6]];
console.log(func[4[1]])