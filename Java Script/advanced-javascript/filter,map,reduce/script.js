// ambil semua elemen li/judul video
const playlist = Array.from(document.querySelectorAll("ul li[data-duration]"))
// pilih hanya yang "programming courses" dan masukkan ke dalam html sebagai jumlah/simpah di dom
let judul = "Programming courses for beginner"
let programmingPlaylist = playlist.filter((e) => e.innerHTML.includes(judul))
// ambil durasi masing2 video
let durasiPlaylist = programmingPlaylist.map(e => {
    return e.getAttribute("data-duration")
})
// ubah string durasi menjadi int, lalu jadikan detik (dikali 60)
.map(e => (parseInt(e) * 60) + ((parseFloat(e) - parseInt(e)) * 100))
// jumlahkan semua detik
.reduce((acc, curr) => acc + curr)
// ubah menjadi jam menit detik
let jam = parseInt(durasiPlaylist / 3600); menit = parseInt((durasiPlaylist % 3600) / 60); detik = ((durasiPlaylist % 3600) % 60)
let durasi = jam + ' : ' + menit + ' : ' + detik
// simpan di dom
console.log(durasi);
const jumlahVideo = document.querySelector('span.jumlah-video')
const totalDurasi = document.querySelector('span.total-durasi')
jumlahVideo.innerHTML = programmingPlaylist.length
totalDurasi.innerHTML = durasi
