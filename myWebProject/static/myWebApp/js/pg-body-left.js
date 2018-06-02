$(document).ready(function () {
    // body左边第一个框的第一项鼠标移进去的时候显示对应内容，移动出去的时候消失
    // $('.pg-body .body-left #classify1').bind('mouseover',function () {
    //     $('.pg-body .left-frist-content #left-frist-item1').children().removeClass('hide');
    // }).bind('mouseout',function () {
    //     $('.pg-body .left-frist-content #left-frist-item1').children().addClass('hide');
    // });
    // // 鼠标移到body左边第一个框内容中时，内容固定住
    // $('.pg-body .left-frist-content #left-frist-item1').bind('mouseover',function () {
    //     $('.pg-body .left-frist-content #left-frist-item1').children().removeClass('hide');
    // }).bind('mouseout',function () {
    //     $('.pg-body .left-frist-content #left-frist-item1').children().addClass('hide');
    // });

    // body左边第一个框鼠标移进去的时候显示对应内容，移动出去的时候消失
    var target;
    var temp;
    $('.pg-body .body-left #classify').children().bind('mouseover',function () {
        // var target=$(self).attr("target");
        // itemName=$(target).attr("target");
        // // console.log($("#"+itemName).children());
        // $("#"+itemName).attr('class','Item');
        target=$(this).attr("target");
        $("#"+target).attr('class','Item');
    }).bind('mouseout',function () {
        $("#"+target).attr('class','Item hide');
    });
    //鼠标移进去的时候固定内容，出来的内容消失
    $('.pg-body .left-frist-content .itemPublic').bind('mouseover',function (){
        temp=$(this).children();
        $(this).children().removeClass("hide")
    }).bind('mouseout',function () {
        $(temp).addClass('hide');
    });
});













