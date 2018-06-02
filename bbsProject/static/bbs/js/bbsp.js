$(document).ready(function () {
   $(".wrap-left .article-show-info button").click(function () {
       var content_text=$("#comment-area").val();
       if(content_text.trim().length < 6) {
           alert("评论字数不能低于6个")
       }//end if
       else{
           token=$("input[name='csrfmiddlewaretoken']").val();
        // 发起AJAX请求
           $.post("/bbs/userComment/",
               {
                   "comment_type":1,
                   article_id:"{{ artical_info.id }}",
                   parent_comment_id:null,
                   "comment":content_text.trim(),
                   "csrfmiddlewaretoken":token
               },
               function (callback) {
                   alert(callback)
               })//end post
       }//end else
   })//end click
});