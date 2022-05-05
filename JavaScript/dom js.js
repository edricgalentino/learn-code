// // DOM Selection

// // 1. doc.getElementById
// // 2. doc.getElementsByTagName
// // 3. doc.getElementsByClassName
// // 4. doc.querySelector
// // 5. doc.querySelectorAll

// // 1. doc.getElementById = element

// const judul = document.getElementById('judul')
// // mengganti style
// judul.style.color = '#222'
// judul.style.backgroundColor = '#bbb'
// // mengganti isi elemen judul
// judul.innerHTML = 'Makan Konate'

// // 2. doc.getElementsByTagName = HTMLCollection

// // const p = document.getElementsByTagName('p')
// // for (let i = 0; i < p.length; i++) {
// //     p[i].style.backgroundColor = 'lightgrey'
// // }

// const h1 = document.getElementsByTagName('h1')[0]
// h1.style.fontFamily = 'timesnewroman'

// // 3. doc.getElementsByClassName = HTMLCollection

// const p1 = document.getElementsByClassName('p1')[0]
// p1.style.fontStyle = 'italic'
// p1.style.fontSize = '50px'
// p1.innerHTML = 'Vincenzo Cassano'

// // 4. doc.querySelector

// const p4 = document.querySelector('#b p')
// p4.style.fontSize = '30px'
// // gabisa kayak gini, harus pake All
// // const p = document.querySelector('p')
// // p.innerHTML = 'bahaya nih kaya gini'

// // 5. doc.querySelectorAll (bisa menyeleksi banyak elemen html)

// const p2 = document.querySelectorAll('p')
// for (let i = 0; i < p2.length; i++) {
//     p2[i].style.backgroundColor = 'lightgrey'
// }
// // all

// DOM MANIPULATION

// 1. element.innerHTML
// const judul = document.getElementById('judul')
// judul.innerHTML = ('Judulllahhhhh')

// 2. element.style.<property CSS>
// const judul = document.getElementById('judul')
// judul.style.backgroundColor = 'red'

// 3. 
// const judul = document.getElementsByTagName('h1')[0]
// // judul.setAttribute('name', 'edric')
// const a = document.querySelector('section#a a')

// DOM MANIPULATION NODE
// menambahkan paragraf baru di akhir section dengan appendChild

// const pBaru = document.createElement('p')
// const isiP = document.createTextNode('Paragraf barunya nih')
// pBaru.appendChild(isiP)
// const sectionA = document.getElementById('a')
// sectionA.appendChild(pBaru)

// menambahkan li di tengah tengah ul

// const liBaru = document.createElement('li');
// const isiLiBaru = document.createTextNode('isi dari listnya dah ni');
// liBaru.appendChild(isiLiBaru);
// const ul = document.querySelector('section#b ul');
// const liDua = ul.querySelector('li:nth-child(2)');
// ul.insertBefore(liBaru, liDua);

// Mengubah p4 menjadi h2

// const h2Baru = document.createElement('h2')
// const isiH2Baru = document.createTextNode('Judul Baru')
// h2Baru.appendChild(isiH2Baru)
// const sectionB = document.getElementById('b')
// const p4 = sectionB.querySelector('p')
// sectionB.replaceChild(h2Baru, p4)

// Menghapus link pada html

// const sectionA = document.getElementById('a')
// const link = sectionA.getElementsByTagName('a')[0]
// sectionA.removeChild(link);

// DOM SELECTION LAINNYA (NEW VERSION)

// 1. parentNode.append() = sama kaya append child, untuk menambahkan elemen baru pada AKHIR section parentNode
// 2. parentNode.prepend() = untuk menambahkan elemen baru pada AWAL section parentNode
// 3. childNode.before(,) = sama kaya insertBefore, menambahkan elemen sebelum
// 4. childNode.after(,) = menambahkan elemen sesudah
// 5. childNode.remove() = menghapus elemen
// 6. childNode.replaceWith(,) = mengganti elemen dengan

// (,) = di isi dengan 2 parameter (elemen baru, elemen lama)

// DOM EVENTS

// const p3 = document.querySelector('section#a .p3')
// p3.addEventListener('click', function () {
//     p3.style.backgroundColor = 'lightgreen'
//     p3.style.color = 'red'
// });

// DOM TRAVERSAL









