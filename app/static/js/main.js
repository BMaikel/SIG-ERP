// Left Sidebard Js
$(document).on("click",".sidebar li", function(){
    $(this).addClass("active").siblings().removeClass("active")
})

// Sidebar toggle
$(document).ready(function() {
    $("#toggleSidebar").click(function(){
        $(".left-menu").toggleClass("hide");
        $(".content-wraper").toggleClass("hide");
    })
})