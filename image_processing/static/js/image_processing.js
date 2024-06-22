$(document).ready(function () {
    $('#image-form').submit(function (event) {
        event.preventDefault(); // Prevent the form from submitting in the traditional way
        var formData = new FormData($(this)[0]);
        
        $.ajax({
            url: $(this).attr('action'),
            type: $(this).attr('method'),
            data: formData,
            processData: false,
            contentType: false,
            success: function (response) {
                $('#processed-image').html('<img src="data:image/png;base64,' + response + '" alt="Processed Image">');
            },
            error: function (xhr, status, error) {
                console.error(xhr.responseText);
            }
        });
    });
});

