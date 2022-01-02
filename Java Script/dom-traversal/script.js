// const closeB = document.querySelector('.close');
// const card = document.querySelector('.card');

// closeB.addEventListener('click', function () {
//     card.style.display = 'none'
// })

// multiple

const closeB = document.querySelectorAll('.close');
// for (let i = 0; i < closeB.length; i++) {
//     closeB[i].addEventListener('click', function (e) {
//         e.target.parentElement.style.display = 'none'
//     })
// }
closeB.forEach(function (eee) {
    eee.addEventListener('click', function (e) {
        e.target.parentElement.style.display = 'none';
        e.preventDefault()
    })
})