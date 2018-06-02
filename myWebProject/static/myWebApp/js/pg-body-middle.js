$(document).ready(function () {
    $(".pg-body .body-middle .middle-Menu ul").children().bind("mousedown",function () {
        $(this).addClass('whiteColor');
        $(this).siblings().removeClass('whiteColor');
        var targetContent=$(this).attr("target");
        // console.log(targetContent)

        // $("#"+targetContent).removeClass('hide');
        // templist=$("#"+targetContent).siblings();
        // console.log(templist);
        // for(var i=0;i<templist.length;i++){
        //     // if (templist[i].attr("middle-Menu-content","None")){
        //     //     templist[i].addClass('hide')
        //     // }
        // }
    })
});