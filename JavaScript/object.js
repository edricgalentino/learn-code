// object, lebih sakti dari array

// latihan pertama

// var dataDiri = {
//     nama : 'Edric Galentino',
//     umur : 18,
//     kelas : 'XII MIPA 1',
//     hobi : ['melatih soft skill', 'latihan coding', 'mempelajari skill baru'],
//     alamat : {
//         jalan : 'Gg. jaim RT/RW 004/02 No.77',
//         kecamatan : 'Pesanggrahan',
//         kelurahan : 'Petukangan Selatan'
//     }
// }
// console.log(dataDiri['alamat']['jalan']);


// MEMBUAT OBJECT

// 1. Functional Object

// var mhs1 = {
//     nama : 'Edric Galentino',
//     umur : 18,
//     makanan : 'Roti'
//     jurusan : 'Teknik Informatika'
// }

// 2. Function Declaration

// function objectMahasiswa(nama, umur, makanan, jurusan) {
//     var mhs = {}
//     mhs.nama = nama;
//     mhs.umur = umur;
//     mhs.makanan = makanan;
//     mhs.jurusan = jurusan;
//     return mhs;
// }
// let mhs2 = objectMahasiswa('Kenji Oby', 11, 'Ayam', 'DKV')
// console.log(mhs2);

// 3. Construction

// function DataMhs(nama, umur, makanan, jurusan) {
//     this.nama = nama;
//     this.umur = umur;
//     this.makanan = makanan;
//     this.jurusan = jurusan;
// }
// const mhs3 = new DataMhs('Nurhayati', 42, 'Seblak', 'Tata Boga');
// console.log(mhs3);

