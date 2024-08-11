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

    // const folder_one = document.getElementById('folder-1');
    // folder_one.addEventListener('click', function() {
    //     console.log("Clicked Folder 1");
    // });

    // const folder_two = document.getElementById('folder-2');
    // folder_two.addEventListener('click', function() {
    //     console.log("Clicked Folder 2");
    // });
});
