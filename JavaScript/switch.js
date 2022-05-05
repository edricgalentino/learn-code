var item = prompt('Masukkan nama makanan/ minuman : \n cth: udang, ayam, bakwan, cilor, sayur sop, seblak')

switch (item) {
    case 'udang':
    case 'ayam':
    case 'sayur sop':
        alert(item + ' adalah makanan SEHAT')
        break;
    case 'bakwan':
    case 'cilor':
    case 'seblak':
        alert(item + ' adalah makanan TIDAK SEHAT')
        break;
    default:
        alert('Nama yang anda masukkan tidak sesuai contoh!')
        break;
}