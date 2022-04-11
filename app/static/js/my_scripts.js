jQuery.noConflict();
var $ = jQuery;
$(function ($) {
    var header = $('header');
    var menuButton = $('.menu-button');
    var menu = $('header nav');
    var headerHeigth = header.outerHeight();

    menuButton.on('click', function (e) {
        e.preventDefault();
        var iconSpan = $(this).find('span');
        var classOn = iconSpan.data('onmenu');
        var classClose = iconSpan.data('closemenu');
        menu.toggleClass('on-menu');
        if (menu.hasClass('on-menu')) {
            iconSpan.removeClass(classOn);
            iconSpan.addClass(classClose);
            menuButton.addClass('closeIcon');
        } else {
            iconSpan.addClass(classOn);
            iconSpan.removeClass(classClose);
            menuButton.removeClass('closeIcon');
        }
        e.stopPropagation();
    });

    $('body,html,header nav a').on('click', function () {
        menu.removeClass('on-menu');
    });

    menu.on('click', function (e) {
        e.stopPropagation();
    });

    anchorNav(headerHeigth);
    function anchorNav(headerHeigth) {
        $('.anchor').on('click', function (e) {
            e.preventDefault();
            var ancla = $(this).attr('href');
            $('body,html').stop(true, true).animate({
                scrollTop: $(ancla).offset().top - headerHeigth
            }, 350);
        });
    }

});

					 
