// latihan pengelolaan angkot dengan object

function Angkot(supir, trayek, penumpang, kas) {
    this.supir = supir;
    this.trayek = trayek;
    this.penumpang = penumpang;
    this.kas = kas;
    this.penumpangNaik = function (namaPenumpang) {
        return this.penumpang.push(namaPenumpang)
    }
    this.penumpangTurun = function (namaPenumpang, bayar) {
        if (this.penumpang.length === 0) {
            return console.log('Angkot masih kosong');
        } else {
            for (let i = 0; i < this.penumpang.length; i++) {
                if (this.penumpang[i] == namaPenumpang) {
                    this.penumpang[i] = undefined;
                    this.kas += bayar;
                    return this.penumpang;
                }
            }
        }
    }
}
let angkot1 = new Angkot('Lionel Messi', ['Ciseeng - Pd. Betung'], [], 0 )
let angkot2 = new Angkot('Neymar', ['Jakarta - Bali'], [], 0 )
angkot1.penumpangNaik('muhammad')
angkot1.penumpangNaik('Muhammad')
angkot1.penumpangTurun('muhammad', 3500)
console.log(angkot1.kas);