jQuery.noConflict();
jQuery(document).ready(function($){								
	"use strict";
	
	//STICKY NAV MENU....
	if(mytheme_urls.stickynav === "enable") {
		$("#header-wrapper").sticky({ topSpacing: 0 });
	}
	
	//MOBILE MENU...
	$('#page-nav > ul').mobileMenu({
      defaultText: 'Navigate to...',
      className: 'mobile-menu',
      subMenuDash: '&ndash;&nbsp;'
	});
								
	//TEXTBOX CLEAR...
	$('input.Textbox, textarea.Textbox').focus(function() {
      if (this.value === this.title) {
        $(this).val("");
      }}).blur(function() {
      if (this.value === "") {
        $(this).val(this.title);
      }
    });
	
	//ISOTOPE CATEGORY CLICK...
	var $container = $('.portfolio-container');	
	var $gw = 20;
	
	if($('.portfolio-container li').hasClass('with-sidebar')) { $gw = 12; }
	
	$('.sorting-container a').click(function(){ 
		$('.sorting-container').find('a').removeClass('active');
		$(this).addClass('active');
		
		var selector = $(this).attr('data-filter');
		$container.isotope({
			filter: selector,
//			animationEngine: 'best-available',			
			animationOptions: {
				duration: 750,
				easing: 'easeOutBack',
				queue: false
			},
			masonry: {
				columnWidth: $('.portfolio-container li').width(),
				gutterWidth: $gw
			}
		});
		return false;
	});

	if($container.length){
		//ISOTOPE...
		$container.isotope({ 
			filter: '*',
//			animationEngine: 'best-available',
			animationOptions: {
				duration: 750,
				easing: 'linear',
				queue: false
			},
			masonry: {
				columnWidth: $('.portfolio-container li').width(),
				gutterWidth: $gw
			}
		});
	}
	
	var $pphoto = $('a[data-gal^="prettyPhoto"]');
	if($pphoto.length){
		//PRETTYPHOTO...
		$("a[data-gal^='prettyPhoto']").prettyPhoto({ 
			theme:"dark_rounded", 
			autoplay_slideshow: false, 
			overlay_gallery: false, 
			show_title: false,
			social_tools: false,
			deeplinking: false
		});
	}
	
	//PARTNERS...
	if($(".carousel-wrapper").length) {
      $('.testimonial-carousel').carouFredSel({
        responsive: true,
		auto: false,
		width: '100%',
		prev: '.test-prev',
		next: '.test-next',
		height: 'auto',
		scroll: {
			fx: 'crossfade'
		},				
		items: {
          visible: {
            min: 1,
			max: 1
          }
        }
      });
      //PORFOLIO CAROUSEL...
      $('.portfolio-carousel').carouFredSel({
        responsive: true,
		auto: false,
		width: '100%',
		prev: '.prev-arrow',
		next: '.next-arrow',
		height: 'auto',
		scroll: 1,				
		items: { width: 220, visible: { min: 1, max: 3 } }
      });
	}
	
	//PORTFOLIO BX SLIDER...
	if(jQuery(".portfolio-slider").length) {
      $('.portfolio-slider').bxSlider({
        auto: true,
        pager: ''
      });
	}
	
	if($(".tabs-framed-container").length)
	{
		$('.tabs-framed-container ul.tabs-framed li:first a').addClass('current');
		$('.tabs-framed-container .list-wrap div:first').removeClass('hide');
		$(".tabs-framed-container").organicTabs({
			"speed": 200
		});
	}
	
	//UI TO TOP PLUGIN...
	$().UItoTop({ easingType: 'easeOutQuart' });
	
	//BUDDHA BAR...
	$("div#bbar-open").click(function(e){
		$(this).hide();	
		$("div#bbar-body").slideDown('slow',function(){ $("div#bbar-close").show(); });
		e.preventDefault();
	});
	
	$("div#bbar-close").click(function(e){
	    $("div#bbar-close").hide();
	    $("div#bbar-body").slideUp('slow');
	    $("div#bbar-open").slideDown();
	    e.preventDefault();
	});
	
	//FOOTER NAV LINE HIDE...
	$('ul.footer-links li:last').addClass('last');
});