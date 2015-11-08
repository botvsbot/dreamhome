var ajaxRequest = function(params) {
    var url = params['url'];
    var data = params['data'];

    var actionType = params['actionType'];
    if (actionType == undefined) {
        actionType = 'post';
    }

    var successAction = params['successAction'];
    $.ajax({
        url: url,
        type: actionType,
        data: JSON.stringify(data),
        contentType: 'application/json',
        dataType: 'json',
        success: function (data, status, xhr) {
            successAction(data);
        }
    });
    return true;
};