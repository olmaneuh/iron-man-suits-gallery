$(document).ready(function() {
    // replace the label text with the file name in the form
    $('#image').on('change', function() {
        var fileName = $(this)[0].files[0].name;
        $(this).next('.custom-file-label').html(fileName);
    });
});