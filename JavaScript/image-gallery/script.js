const downContentImg = document.querySelector(".down-content")
const upContentImg = document.querySelector(".up-content img")

downContentImg.addEventListener('click', function (e) {
    // upContentImg.src = e.target.src; (lebih singkat)
    const attribute = e.target.getAttribute('src');
    upContentImg.setAttribute('src', attribute);
    upContentImg.classList.add('fade');
    setTimeout(() => {
        upContentImg.classList.remove('fade');
    }, 500);
})