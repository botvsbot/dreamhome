/**
 * Created by rganesh on 11/7/15.
 */
$.getScript("../static/js/utils.js", function () {

    $('.zipcode-submit-btn').on('click', function () {
        console.log("Button submitted");
        var data = {
            "zipcode_input": $('input[name="zipcode_input"]').val(),
            "priorities": $('input[name="priorities"]').val(),
            "radius": $("#radius option:selected").text()
        };
        console.log(data);
        successFunc = function (data) {
            window.location = "/zipcode/" + data.zip;
        };
        var ajax_params = {
            'actionType': 'post',
            'url': '/zipcode/',
            'data': data,
            'successAction': successFunc
        };
        ajaxRequest(ajax_params)
    });
});