let penumpang = []
let tambahPenumpang = function (namaPenumpang, penumpang) {
    if (penumpang.length == 0) {
        return penumpang.push(namaPenumpang);
    } else {
        for (let i = 0; i < penumpang.length; i++) {
            if (penumpang[i] == undefined) {
                if (penumpang[i] !== namaPenumpang) {
                    return penumpang[i]=namaPenumpang 
                } else if (penumpang[i] == namaPenumpang) {
                    return console.log(namaPenumpang+' sudah ada di dalam angkot')
                }
            }
            else if (penumpang[i]==namaPenumpang) {
                return console.log(namaPenumpang+' sudah ada di dalam angkot')
            }
            else if (i == penumpang.length-1) {
                return penumpang.push(namaPenumpang)
            }
        }
    }
}
let hapusPenumpang = function (namaPenumpang, penumpang) {
    if (penumpang.length == 0) {
        return console.log('Angkot sedang kosong');
    } else {
        for (let p = 0; p < penumpang.length; p++) {
            if (penumpang[p]==namaPenumpang) {
                return penumpang[p] = undefined 
            } else if (p == penumpang.length-1) {
                return console.log(namaPenumpang+' sejak awal tidak ada di dalam angkot');
            }
        }
    }
}
tambahPenumpang('makise', penumpang)
tambahPenumpang('raisa', penumpang)
hapusPenumpang('makise', penumpang)
tambahPenumpang('raisa', penumpang)
tambahPenumpang('muhammad', penumpang)
tambahPenumpang('makise', penumpang)

console.log(penumpang)