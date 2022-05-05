const tombol = document.querySelector('.tombol');
const circle = document.getElementsByClassName('circle')[0];
tombol.addEventListener('click', function () {
    circle.classList.toggle('toggle');
    document.body.classList.toggle('ubah-warna');
});

// membuat tombol acak warna

const buttonAcak = document.createElement('button');
const textButton = document.createTextNode('Acak warna');
const r = parseInt(Math.random() * 255 + 1);
buttonAcak.append(textButton)
buttonAcak.setAttribute('type', 'button')
document.body.append(buttonAcak)
buttonAcak.addEventListener('click', function () {
    const r = parseInt(Math.random() * 255 + 1);
    const g = parseInt(Math.random() * 255 + 1);
    const b = parseInt(Math.random() * 255 + 1);
    document.body.style.backgroundColor = 'rgb('+ r +','+ g +','+ b +')'
});

// range value color

// const sMerah = document.querySelector('input[name=merah]');
// const sHijau = document.querySelector('input[name=hijau]');
// const sBiru = document.querySelector('input[name=biru]');

// sMerah.addEventListener('input', function () {
//     const r = sMerah.value;
//     const g = sHijau.value;
//     const b = sBiru.value;
//     document.body.style.backgroundColor = 'rgb('+ r +','+ g +','+ b +')'
// })
// sHijau.addEventListener('input', function () {
//     const r = sMerah.value;
//     const g = sHijau.value;
//     const b = sBiru.value;
//     document.body.style.backgroundColor = 'rgb('+ r +','+ g +','+ b +')'
// })
// sBiru.addEventListener('input', function () {
//     const r = sMerah.value;
//     const g = sHijau.value;
//     const b = sBiru.value;
//     document.body.style.backgroundColor = 'rgb('+ r +','+ g +','+ b +')'
// })