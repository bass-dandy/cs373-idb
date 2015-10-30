function parallax() {
    var scrolled = $(window).scrollTop();
    $(".parallax-bg").css("transform", "translateY(-" + scrolled * 0.2 + "px)");
}

$(window).bind('scroll', function(e) {
    parallax();
});
