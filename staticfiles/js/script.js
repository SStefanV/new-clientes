/*-------------------------------------|
* Al scripts here will extends all pages
---------------------------------------|*/

// If no client, show a message

$(document).ready(function () {
    var verify = $("#chk_td").length;
    if (verify == 0) {
        $('#no_data').text('Cliente no encontrado!! ');
    }
});

// Real time
setInterval(function () {
    var date = new Date();
    $('#clock').html(
        (date.getHours() < 10 ? '0' : '') + date.getHours() + ':' + (date.getMinutes() < 10 ? '0' : '') + date.getMinutes() + ':' + (date.getSeconds() < 10 ? '0' : '') + date.getSeconds()
    );
}, 500);
