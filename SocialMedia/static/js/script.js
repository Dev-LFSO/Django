function adjustTextareaHeight(textarea) {
    textarea.style.height = 'auto';
    textarea.style.height = (textarea.scrollHeight - 15) + 'px';
}

document.addEventListener('DOMContentLoaded', function () {
    var textareas = document.querySelectorAll('textarea.post-content');
    textareas.forEach(function (textarea) {
        adjustTextareaHeight(textarea);
    });
});