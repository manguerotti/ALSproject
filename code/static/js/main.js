window.onload = function() {
    var errorMsg = document.getElementsByClassName('dvErrorMsg')[0];
    errorMsg.addEventListener('click', function() {
        this.style.display = 'none';
    });

    setTimeout(function() {
        errorMsg.style.display = 'none';
    }, 5000);
}

function openModal() {
    document.getElementById('myModal').style.display = "block";
}

function closeModal() {
    document.getElementById('myModal').style.display = "none";
}

window.onclick = function(event) {
    if (event.target == document.getElementById('myModal')) {
        document.getElementById('myModal').style.display = "none";
    }
}

const darkTheme = () => {
    document.querySelector("body").setAttribute('data-bs-theme', 'dark');
    document.querySelector('#dl-icon').setAttribute('class', 'bi bi-sun-fill fs-1');
}

const lightTheme = () => {
    document.querySelector("body").setAttribute('data-bs-theme', 'light');
    document.querySelector('#dl-icon').setAttribute('class', 'bi bi-moon-fill fs-1');
}

const changeTheme = () => {
    const theme = document.querySelector("body").getAttribute('data-bs-theme');
    if (theme === 'dark') {
        lightTheme();
    } else {
        darkTheme();
    }
}