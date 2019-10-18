jQuery.noConflict();
jQuery(document).ready(function($) {
  "use strict";
  
  //SKILL BARS...
  animateSkillBars();
  $(window).scroll(function(){ animateSkillBars(); });
  
  //TABS...
  if($('ul.tabs').length > 0) {
    $('ul.tabs').tabs('> .tabs-content');
  }
  
  if($('ul.tabs-frame').length > 0){
    $('ul.tabs-frame').tabs('> .tabs-frame-content');
  }
  
  if($('.tabs-vertical-frame').length > 0){
    
    $('.tabs-vertical-frame').tabs('> .tabs-vertical-frame-content');
    
    $('.tabs-vertical-frame').each(function(){
      $(this).find("li:first").addClass('first').addClass('current');
      $(this).find("li:last").addClass('last');
    });
    
    $('.tabs-vertical-frame li').click(function(){
      $(this).parent().children().removeClass('current');
      $(this).addClass('current');
    });
  }
  
  //Custom tab jquery works...
  if($('.custom-tabs-frame').length > 0){
    
    $('.custom-tabs-frame').tabs('> .custom-tabs-content').parent();
    
    $('.custom-tabs-frame').each(function(){
      $(this).find("li:first").addClass('first').addClass('current');
      $(this).find("li:last").addClass('last');
    });
    
    $('.custom-tabs-frame li').click(function(){
      $(this).parent().children().removeClass('current');
      $(this).addClass('current');
    });
  }
  
  //TOGGLES...
  $('.toggle').toggle(function(){ $(this).addClass('active'); },function(){ $(this).removeClass('active'); });
  $('.toggle').click(function(){ $(this).next('.toggle-content').slideToggle(); });
  $('.toggle-frame-set').each(function(){
    var $this = $(this),
        $toggle = $this.find('.toggle-accordion');
    
    $toggle.click(function(){
      if( $(this).next().is(':hidden') ) {
        $this.find('.toggle-accordion').removeClass('active').next().slideUp();
        $(this).toggleClass('active').next().slideDown();
      }
      return false;
    });
    
    //ACTIVATE FIRST...
    $this.find('.toggle-accordion:first').addClass("active");
    $this.find('.toggle-accordion:first').next().slideDown();
  });
  
  //TOOLTIP...
  if($(".tooltip-bottom").length){
    $(".tooltip-bottom").each(function(){	$(this).tipTip({maxWidth: "auto"}); });
  }
  
  if($(".tooltip-top").length){
    $(".tooltip-top").each(function(){ $(this).tipTip({maxWidth: "auto",defaultPosition: "top"}); });
  }
  
  if($(".tooltip-left").length){
    $(".tooltip-left").each(function(){ $(this).tipTip({maxWidth: "auto",defaultPosition: "left"}); });
  }
  
  if($(".tooltip-right").length){
    $(".tooltip-right").each(function(){ $(this).tipTip({maxWidth: "auto",defaultPosition: "right"}); });
  }
});

function animateSkillBars(){
  "use strict";
  
  var applyViewPort = ( jQuery("html").hasClass('csstransforms') ) ? ":in-viewport" : "";
  jQuery('.progress'+applyViewPort).each(function(){
    var progressBar = jQuery(this),
        progressValue = progressBar.find('.bar').attr('data-value');
    
    if (!progressBar.hasClass('animated')) {
      progressBar.addClass('animated');
      progressBar.find('.bar').animate({width: progressValue + "%"},600,function(){ progressBar.find('.bar-text').fadeIn(400); });
    }
	
  });
}