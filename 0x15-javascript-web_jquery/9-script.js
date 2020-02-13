$(function () {
    $.ajax({
        type: 'GET',
        url: 'https://fourtonfish.com/hellosalut/?lang=fr',
        success: function (data) {
                console.log('success', data.hello);
                $('div#hello').text(data.hello);
        }
    });
});