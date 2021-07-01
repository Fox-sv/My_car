$(document).ready(function () {
    var append_increment = 0;
    setInterval(function() {
        $.ajax({
            type: "GET",
            url: ALARM_URL,
            data: {'append_increment': append_increment}
        })
        .done(function(response) {
            $('#resu').load(' #resu');
            append_increment += 1;
        });
    }, 1000)
  })
