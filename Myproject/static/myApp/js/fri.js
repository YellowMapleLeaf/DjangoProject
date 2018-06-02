$(document).ready(function () {

    $("#btn").bind("click",function () {
        $.ajax({
            type:"get",
            url:"/friendsinfo/",
            dataType:"json",
            success:function(data) {
                console.log(data);
                var d = data["data"];

                for(var i = 0; i < d.length;i++){
                    temp='<p>'+d[i][0]+'---------'+d[i][1]+'</p>';
                    $("#btn").after(temp);
                    // document.write('<p>'+d[i][0]+'</p>')
                }
            }
        })
    })
});