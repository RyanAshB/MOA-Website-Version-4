
document.addEventListener('DOMContentLoaded', (event) => {
    const parentContainer = document.querySelector('.read-more-container');

    parentContainer.addEventListener('click', event => {
        const current = event.target;

        const isReadMoreBtn = current.className.includes('read-more-btn');

        if (!isReadMoreBtn) return;

        const currentText = event.target.parentNode.querySelector('.read-more-text');

        currentText.classList.toggle('read-more-text--show');

        current.textContent = current.textContent.includes('Read More') ? "Read Less..." : "Read More...";
    });
});

function openPopup_1() {
    let popup = document.getElementById('hte-popup-1');
    popup.classList.add('hte-open-popup');  
}

function closePopup_1() {
    const popup = document.getElementById('hte-popup-1');
    popup.classList.remove('hte-open-popup');  
}

function openPopup_icons() {
    let popup = document.getElementById('hte-popup-icons');
    popup.classList.add('hte-popup-icons-open');  
}

document.addEventListener('click', function(event) {
    let popup = document.getElementById('hte-popup-icons');
    if (!popup.contains(event.target) && !event.target.closest('.service')) {
        popup.classList.remove('hte-popup-icons-open');
    }
});

document.addEventListener('click', function(event) {
    let popup = document.getElementById('hte-popup-1');
    if (!popup.contains(event.target) && !event.target.closest('.hte-popup-button')) {
        popup.classList.remove('hte-open-popup');
    }
});

