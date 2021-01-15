$(window).scroll(function() {
  var scrollTop =  0;
  $(window).scroll(function(event){
    var scroll = $(this).scrollTop();
    if (scroll <= scrollTop && scroll >= 600) {
      $(".landingPageNav").addClass("landingPageNavUp");
    }else if (scroll >=600 && scrollTop != 0){
      $(".landingPageNav").removeClass("landingPageNavUp");
      $(".landingPageNav").addClass("landingPageNavDown");
    }else if (scrollTop != 0){
      $(".landingPageNav").removeClass("landingPageNavDown");
      $(".landingPageNav").removeClass("landingPageNavUp");
    }
    scrollTop = scroll
  });
});

(window).scroll(function() {
  var scrollTop =  0;
  $(window).scroll(function(event){
    var scroll = $(this).scrollTop();
    if (scroll <= scrollTop && scroll >= 600) {
      $(".navbar").addClass("navUp");
    }else if (scroll >=600 && scrollTop != 0){
      $(".navbar").removeClass("navUp");
      $(".navbar").addClass("navDown");
    }else if (scrollTop != 0){
      $(".navbar").removeClass("navDown");
      $(".navbar").removeClass("navUp");
    }
    scrollTop = scroll
  });
});
