function postData(payload, url) {
    var token = $('input[name="csrfmiddlewaretoken"]').attr('value')
    
    return $.ajax({
        headers: { "X-CSRFToken": token },
        type: "POST",
        dataType: "json",
        url: url,
        data: JSON.stringify(payload),
        contentType: "application/json; charset=utf-8",
        beforeSend: function () {
        },
        complete: function () {
        },
        error: function (error) {
            console.log(error)
        }
    });
}