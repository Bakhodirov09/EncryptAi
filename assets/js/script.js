const imageInput = document.querySelector('.selected_image');
const imgElement = document.querySelector('.image');
const footer = document.querySelector('footer')
const encrypt_info = document.querySelector('.encrypt-info')
const bttn = document.querySelector('.bttn')
const button = document.querySelector('.btn')
const textarea = document.querySelector('.message-1')
const message = document.querySelector('.message')

if (textarea) {
    textarea.addEventListener('keyup', e => {
        textarea.style.height = 'auto';
        let scHeight = e.target.scrollHeight;
        if (scHeight >= '104') {
            footer.style.marginTop = '-140px'
            footer.style.height = '710px'
        };
        textarea.style.height = `${scHeight}px`;
    });
}

if (message) {
    message.style.height = '200px';
    message.style.cursor = 'text';
    footer.classList.add('active');
}

// Add event listener to the file input
if (imageInput) {
    imageInput.addEventListener('change', function () {
        // Check if a file is selected
        if (this.files && this.files[0]) {
            // Get the selected file
            var selectedFile = this.files[0];

            // Create a FileReader to read the file
            var reader = new FileReader();

            // Set up the FileReader to load when it's done loading
            reader.onload = function (event) {
                imgElement.src = event.target.result;
            };

            imgElement.classList.add('active');
            footer.classList.add('active');
            if (encrypt_info) {
                encrypt_info.classList.add('active');
            }
            if (button) {
                button.classList.add('active');
            }
            if (bttn) {
                bttn.classList.add('active');
            }
            reader.readAsDataURL(selectedFile);
        }
    });
}