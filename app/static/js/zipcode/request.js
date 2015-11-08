/**
 * Created by rganesh on 11/7/15.
 */
$.getScript("../static/js/utils.js", function () {


    console.log("Here");
    $.getJSON("/zipcode/shpdata", function(json) {
    console.log("Inside");
    console.log(json); // this will show the info it in firebug console
    });

    $('.zipcode-submit-btn').on('click', function () {
        console.log("Button submitted");
        var data = {
            "zipcode": $('input[name="zipcode"]').val(),
            "priorities": $('input[name="priorities"]').val()
        };
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