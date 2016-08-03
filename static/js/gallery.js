$('a.gallery').featherlightGallery({
    previousIcon: '«',
      nextIcon: '»',
      galleryFadeIn: 300,
      openSpeed: 300
});

$.featherlightGallery.prototype.afterContent = function() {
  var caption = this.$currentTarget.find('img').attr('alt');
  this.$instance.find('.caption').remove();
  $('<div class="caption">').text(caption).appendTo(this.$instance.find('.featherlight-content'));
};