document.addEventListener('DOMContentLoaded', function() {
    const folders = document.querySelectorAll('.folder');
    
    folders.forEach(function(folder) {
        folder.addEventListener('click', function() {
            const content = folder.querySelector('.folder-content')

            if (!folder.classList.contains('open')) {
                folder.classList.add('open');
                content.classList.add('isVisible');
                console.log("Adding open");
            } else {
                folder.classList.remove('open');
                content.classList.remove('isVisible');
            }
        });
    });


    const urlParams = new URLSearchParams(window.location.search);
    const modalToShow = urlParams.get('modal');

    // Check if the "modal" parameter is set to "incentives"
    if (modalToShow === 'incentives') {
        // Trigger the modal to open
        const incentivesModal = new bootstrap.Modal(document.getElementById('exampleModal5'));
        incentivesModal.show();
    }
});
