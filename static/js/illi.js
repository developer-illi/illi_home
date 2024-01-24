$(document).ready(function(){
    
    // slick js slider
        $('.main_slider').slick({
            dots: true,
            infinite: false,
            draggable: false,
            speed: 300,
            slidesToShow: 4,
            slidesToScroll: 1,
            responsive: [
                {
                    breakpoint: 1600,
                    settings: {
                        slidesToShow: 3
                    }
                },
                {
                    breakpoint: 1024,
                    settings: {
                        slidesToShow: 2
                    }
                }, 
                {
                    breakpoint: 768,
                    settings: {
                        slidesToShow: 2,
                        draggable: true
                    }
                }
            ]
        });
        
        // 변수 선언
        var nav_wrap = $('#nav_wrap');
        var gnb = $('.gnb > li > a');
        var header = $('header');
        
        // btn_nav 클릭시 네비메뉴 나오기
        $('.btn_nav').click(function(){
            nav_wrap.addClass('nav_on')
        });
            
        // close 클릭시 네비메뉴 사라지기
        $('.close').click(function(){
            nav_wrap.removeClass('nav_on')
            $('.sub_wrap').parent('li').removeClass('on')
        });
    
        // 모바일 메뉴 클릭하면 서브메뉴 나오기
        gnb.click(function(){
            if(nav_wrap.hasClass('nav_on') == true ){
                gnb.parent('li').removeClass('on')
                $(this).parent('li').stop().toggleClass('on')
            }
        });
        
        // 화면사이즈 1024 이상, close 버튼 클릭
        $(window).resize(function(){
            var win_w = $(window).width()
            if(win_w >= 1024){
                $('.close').click()
            }
        });
    
        $(window).scroll(function(){
            
            // 스크롤의 위치
            var win_top = $(window).scrollTop()
            
            // 스크롤시 헤더 스타일 변경
            if(win_top){
                header.addClass('active');
            } else {
                header.removeClass('active');
            }
        });
    
});




























