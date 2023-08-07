$(document).ready(function(){
    $('.tap>li>a').click(function(){
        $(this).parent().addClass('active');
        $(this).parent().siblings().removeClass('active');
    });
});