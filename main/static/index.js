let menuicn = document.querySelector(".menuicn");
let nav = document.querySelector(".navcontainer");

menuicn.addEventListener("click", () => {
    nav.classList.toggle("navclose");
})

function setActive(element) {
    // Remove 'active' class from all nav options
    const navOptions = document.querySelectorAll('.nav-option');
    navOptions.forEach(option => {
        option.classList.remove('option1'); // Change to your default class if necessary
    });

    // Add 'active' class to the clicked element
    element.classList.add('option1');
}
