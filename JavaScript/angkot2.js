var jmlAngkot = 10
var noAngkot = 1
var AngkotBeroperasi = 6

// while (noAngkot <= AngkotBeroperasi) {
//     console.log( 'Angkot No. ' + noAngkot + ' beroperasi dengan baik' )
// noAngkot++    
// }
// for (noAngkot = AngkotBeroperasi + 1; noAngkot <= jmlAngkot ; noAngkot++) {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang tidak beroperasi')    
// }


// angkot 4
// for (noAngkot ; noAngkot <= jmlAngkot; noAngkot++) {
   
//     if (noAngkot <= AngkotBeroperasi ) {
//     console.log( 'Angkot No. ' + noAngkot + ' beroperasi dengan baik' )
// }   
//     else if (noAngkot === 8) {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang lembur' )
// }  
//     else {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang tidak beroperasi')   
// }
// }

// angkot 5
// for (noAngkot ; noAngkot <= jmlAngkot; noAngkot++) {
   
//     if (noAngkot <= AngkotBeroperasi) {
//     console.log( 'Angkot No. ' + noAngkot + ' beroperasi dengan baik' )
// }   
//     else if (noAngkot === 8 || noAngkot === 10) {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang lembur' )
// } 
//     else {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang tidak beroperasi')   
// }
// }

// angkot 6 versi saya
for (noAngkot ; noAngkot <= jmlAngkot; noAngkot++) {
   
    if (noAngkot <= AngkotBeroperasi ^ noAngkot === 5 ) {
    console.log( 'Angkot No. ' + noAngkot + ' beroperasi dengan baik' )
}   
    else if (noAngkot === 8 || noAngkot === 10 || noAngkot === 5) {
    console.log( 'Angkot No. ' + noAngkot + ' sedang lembur' )
} 
    else {
    console.log( 'Angkot No. ' + noAngkot + ' sedang tidak beroperasi')   
}
}
// angkot 6 versi Pak Sandhika
// for (noAngkot ; noAngkot <= jmlAngkot; noAngkot++) {
   
//     if (noAngkot <= AngkotBeroperasi && noAngkot !== 5 ) {
//     console.log( 'Angkot No. ' + noAngkot + ' beroperasi dengan baik' )
// }   
//     else if (noAngkot === 8 || noAngkot === 10 || noAngkot === 5) {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang lembur' )
// } 
//     else {
//     console.log( 'Angkot No. ' + noAngkot + ' sedang tidak beroperasi')   
// }
// }


