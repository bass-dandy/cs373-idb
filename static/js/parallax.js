function parallax() {
    var scrolled = $(window).scrollTop();
    $(".parallax-bg").each(function() {
        $(this).css("transform", "translateY(" + scrolled * $(this).data("speed") + "px)");
    });
}

$(window).bind('scroll', function(e) {
    window.requestAnimationFrame(parallax);
});
